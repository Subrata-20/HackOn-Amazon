# import streamlit as st
# import boto3
# import uuid
# import cv2
# import numpy as np
# from PIL import Image
# from io import BytesIO
# import os

# # AWS CONFIG
# AWS_ACCESS_KEY = ""
# AWS_SECRET_KEY = ""
# BUCKET_NAME = ""
# FOLDER_NAME = "seller_images"
# DOCUMENT_FOLDER = "documents"
# LIVE_FOLDER = "live_photos"

# # Initialize clients
# s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
# rekognition = boto3.client("rekognition", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY,region_name='us-east-1')

# # Upload helper
# def upload_image(file_bytes, filename, folder):
#     key = f"{folder}/{filename}"
#     s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=file_bytes)
#     return key

# # Compare faces
# def compare_faces(source_key, target_key):
#     response = rekognition.compare_faces(
#         SourceImage={'S3Object': {'Bucket': BUCKET_NAME, 'Name': source_key}},
#         TargetImage={'S3Object': {'Bucket': BUCKET_NAME, 'Name': target_key}},
#         SimilarityThreshold=70
#     )
#     return response['FaceMatches']

# # Webcam capture
# def capture_image():
#     cap = cv2.VideoCapture(0)
#     st.info("Press 'q' to capture.")
#     img = None
#     while True:
#         ret, frame = cap.read()
#         cv2.imshow("Press 'q' to capture", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             img = frame
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#     return img

# # Load all document images in S3 (as database)
# def list_document_images():
#     response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=DOCUMENT_FOLDER+'/')
#     if 'Contents' not in response:
#         return []
#     return [obj['Key'] for obj in response['Contents'] if obj['Key'].endswith(('jpg', 'jpeg', 'png'))]

# # Streamlit UI
# st.title("🕵️‍♂️ Fraud Detection with Database Image Matching")

# # Step 1: Upload New Document (optional)
# doc_image = st.file_uploader("Upload New Document to Database", type=["jpg", "jpeg", "png"])
# if doc_image and st.button("Add to Database"):
#     doc_bytes = doc_image.read()
#     doc_filename = f"{uuid.uuid4()}_{doc_image.name}"
#     doc_key = upload_image(doc_bytes, doc_filename, DOCUMENT_FOLDER)
#     st.success(f"✅ Uploaded as {doc_key}")

# # Step 2: Capture real-time photo
# if st.button("📸 Capture Real-Time Photo and Match with Database"):
#     captured = capture_image()
#     if captured is not None:
#         st.image(captured, caption="Captured Image", channels="BGR")

#         _, buffer = cv2.imencode(".jpg", captured)
#         live_bytes = BytesIO(buffer.tobytes())

#         # Upload live image
#         live_filename = f"{uuid.uuid4()}_live.jpg"
#         live_key = upload_image(live_bytes.getvalue(), live_filename, LIVE_FOLDER)

#         # Compare with each document in database
#         doc_keys = list_document_images()
#         best_match = None
#         highest_similarity = 0

#         for doc_key in doc_keys:
#             matches = compare_faces(doc_key, live_key)
#             if matches:
#                 similarity = matches[0]["Similarity"]
#                 if similarity > highest_similarity:
#                     highest_similarity = similarity
#                     best_match = doc_key

#         if best_match:
#             st.success(f"✅ Match Found in Database! Similarity: {highest_similarity:.2f}%")
#             # Show matched image
#             image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{best_match}"
#             st.image(image_url, caption=f"Matched with: {os.path.basename(best_match)}")
#         else:
#             st.error("❌ No Match Found in Database! Fraud Suspected.")



import streamlit as st
import boto3
import uuid
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import os

# AWS CONFIG (replace with environment variables or a safer method in production)
AWS_ACCESS_KEY = "YOUR_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"
REGION = "us-east-1"
BUCKET_NAME = "hackon0101"
DOCUMENT_FOLDER = "documents"
LIVE_FOLDER = "live_photos"

# Initialize AWS clients
s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
rekognition = boto3.client("rekognition", aws_access_key_id=AWS_ACCESS_KEY,
                           aws_secret_access_key=AWS_SECRET_KEY, region_name=REGION)

# Upload image to S3
def upload_image(file_bytes, filename, folder):
    key = f"{folder}/{filename}"
    s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=file_bytes)
    return key

# Compare two faces using Rekognition
def compare_faces(source_key, target_key):
    response = rekognition.compare_faces(
        SourceImage={'S3Object': {'Bucket': BUCKET_NAME, 'Name': source_key}},
        TargetImage={'S3Object': {'Bucket': BUCKET_NAME, 'Name': target_key}},
        SimilarityThreshold=70
    )
    return response['FaceMatches']

# Capture image from webcam
def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Unable to access webcam.")
        return None

    st.info("Press 'q' in the webcam window to capture an image.")
    img = None
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to read from webcam.")
            break

        cv2.imshow("Press 'q' to capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            img = frame
            break

    cap.release()
    cv2.destroyAllWindows()
    return img

# List document images in S3
def list_document_images():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=DOCUMENT_FOLDER + '/')
    if 'Contents' not in response:
        return []
    return [obj['Key'] for obj in response['Contents'] if obj['Key'].lower().endswith(('.jpg', '.jpeg', '.png'))]

# UI starts here
st.title("🕵️‍♂️ Fraud Detection: Match Live Image with Database")

# Upload new document image
doc_image = st.file_uploader("📄 Upload New Document to Database", type=["jpg", "jpeg", "png"])
if doc_image and st.button("📁 Add to Database"):
    doc_bytes = doc_image.read()
    doc_filename = f"{uuid.uuid4()}_{doc_image.name}"
    doc_key = upload_image(doc_bytes, doc_filename, DOCUMENT_FOLDER)
    st.success(f"✅ Document uploaded as `{doc_key}`")

# Capture and match image
if st.button("📸 Capture Real-Time Photo and Match"):
    captured = capture_image()
    if captured is not None:
        st.image(captured, caption="Captured Image", channels="BGR", use_container_width=True)

        # Convert and upload
        _, buffer = cv2.imencode(".jpg", captured)
        live_bytes = BytesIO(buffer.tobytes())
        live_filename = f"{uuid.uuid4()}_live.jpg"
        live_key = upload_image(live_bytes.getvalue(), live_filename, LIVE_FOLDER)

        # Match with documents
        doc_keys = list_document_images()
        best_match = None
        highest_similarity = 0.0

        for doc_key in doc_keys:
            try:
                matches = compare_faces(doc_key, live_key)
                if matches:
                    similarity = matches[0]["Similarity"]
                    if similarity > highest_similarity:
                        highest_similarity = similarity
                        best_match = doc_key
            except Exception as e:
                st.warning(f"⚠️ Could not compare with {doc_key}: {e}")

        if best_match:
            st.success(f"✅ Match Found! Similarity: {highest_similarity:.2f}%")
            image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{best_match}"
            st.image(image_url, caption=f"Matched with: {os.path.basename(best_match)}", use_container_width=True)
        else:
            st.error("❌ No Match Found in Database! Fraud Suspected.")
