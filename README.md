
# Amazon GreenX: The AI Hub for Sustainable Shopping

**Team-0101**: Bisal Prasad | Chinmoy Dutta | Subrata Lodh

![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Platform](https://img.shields.io/badge/Platform-AWS%20%7C%20React%20%7C%20Python-orange)



**GreenX** is a full-stack AI and Blockchain ecosystem integrated into Amazon to solve the critical challenges of sustainable e-commerce. It transforms the shopping experience by providing Adv. Recommendation system, Product Grading System, verifiable trust, intelligent waste reduction, and powerful incentives for both consumers and sellers.

**OUR MAIN TARGET IS END-TO-END SOLUTION TO THE PROBLEM OF THE CUSTOMER AND THE SELLER**
[Team-0101_NIT-SILCHAR.pdf](https://github.com/user-attachments/files/20851612/Team-0101_NIT-SILCHAR.pdf)

---
### Key Objectives

*   **EcoChain Trace & GreenScore™ System:** An AI-powered grading system (A++ to D) based on 8 sustainability metrics, with results secured on a blockchain for ultimate transparency.
*   **EcoSense AI for Fraud Detection:** A robust seller verification system using AWS Rekognition for identity checks and AES-256 encryption to secure data and ensure marketplace integrity.
*   **GreenGather AI Recommendation Engine:** A personalized LLM-based assistant that suggests sustainable product alternatives and organizes group buying to reduce emissions.
*   **RePack AI for Waste Reduction:** A 3D vision system (PyTorch3D) that calculates optimal packaging sizes and provides intelligent recycling/disposal guides.
*   **CarbonKarma AI for Impact Tracking:** A multi-modal AI that estimates a product's carbon footprint from images or text, displayed on a personal user dashboard.
*   **GreenCoin Rewards System:** A gamified economy where users earn and redeem coins for making sustainable choices, fostering engagement and loyalty.
---

### Other Achieved Features
*   **Establish Verifiable Trust with an Advanced AI Grading System:** Eliminate greenwashing with a hybrid AI grading system combining images, text, and metadata. NLP (via LLM) verifies sustainability claims, vision models (e.g., CLIP, YOLOv8) detect packaging and eco-labels, and GNNs analyze supply chain data. Grading uses GreenScore™-style weighted logic with AI-powered claim checks and missing data inference—secured on a blockchain-backed ledger.

*   **Deliver Hyper-Personalized Recommendations with an LLM-Powered Assistant:** Implement an advanced recommendation system, **GreenGather AI**, that goes beyond simple suggestions. It uses LLMs to understand user behavior and values, suggesting sustainable alternatives, organizing low-emission group buys, and personalizing the entire green shopping journey. **HSTU — "Actions Speak Louder than Words: Trillion‑Parameter Sequential Transducers for Generative Recommendations"**, Zhai et al., arXiv (Feb 2024). [📄 Full paper](https://arxiv.org/abs/2402.17152)

*   **Ensure Marketplace Integrity with AI-Powered Security:** Automate seller verification and fraud detection using **EcoSense AI**. This system leverages **AWS Rekognition** for robust identity verification and secures all sensitive data with enterprise-grade **AWS-KMS encryption** to build a safe and trustworthy platform.

*   **Engineer Radical Waste Reduction with 3D Vision:** Drastically cut down on plastic and material waste by implementing **RePack AI**. This system uses **3D Computer Vision (PyTorch3D)** to calculate optimal packaging sizes, minimizing waste, and employs graph algorithms to create efficient, low-carbon return logistics.

*   **Drive Engagement Through Gamified Impact Tracking:** Incentivize sustainable behavior with **CarbonKarma AI** and the `GreenCoin` rewards system. This feature provides real-time carbon footprint analysis from product data and empowers users with a personal dashboard, turning climate action into a rewarding and transparent experience.<!-- filepath: c:\Users\Asus\Desktop\new_projects\hack on backend\readme.md -->

---

## 💡 PROJECT OVERVIEW

GreenX is a suite of five specialized AI and Blockchain modules that work in concert to create a transparent, efficient, and rewarding sustainable marketplace. It's not a single monolithic AI; it's a precise, modular ecosystem built for scale and accuracy.

### Key AI Features

#### 🔗 1. EcoChain Trace: Blockchain for Verifiable Trust
EcoChain provides an immutable, transparent ledger for product certification. It ends greenwashing by giving every eco-product a verifiable history.
*   **GreenScore™:** An A++ to D grading system based on 8 key sustainability metrics.
*   **Digital Certificates:** Blockchain-verified certificates for products and sellers, accessible via QR code.
*   **Consumer Transparency:** Buyers can trace a product's entire lifecycle, from raw materials to their doorstep.

#### ✅ 2. EcoSense AI: AI for Seller Validation & Fraud Detection
EcoSense automates the onboarding of genuine eco-sellers, ensuring the integrity of the GreenX marketplace.
*   **AI-Powered Verification:** Uses **AWS Rekognition** and PhotoDNA to compare seller selfies with official documents, preventing identity fraud.
*   **Secure Data Handling:** All sensitive seller data (PAN, GST) is encrypted using **AES-256 via AWS KMS**, ensuring enterprise-grade security.
*   **Route Optimization:** Uses Dijkstra's algorithm to suggest the most efficient logistics routes for new sellers.

#### 🌍 3. CarbonKarma AI: AI for Product Carbon Footprint Analysis
CarbonKarma gives consumers real-time insight into the environmental impact of their purchases, turning abstract data into tangible motivation.
*   **Multi-Modal Input:** Estimates CO₂ footprint from either a **product image** or a **text description** using a fine-tuned LLM (Gemini).
*   **Impact Dashboard:** A personal dashboard showing users their cumulative impact (e.g., "You've saved 12kg of CO₂ this month, equivalent to planting 3 trees").
*   **Gamification:** Drives behavioral change by making sustainability a rewarding and emotionally resonant experience.

#### 📦 4. RePack AI: AI for Intelligent Waste Reduction
RePack AI tackles packaging waste at the source by using 3D vision to optimize packaging for every single item.
*   **3D Vision Analysis:** Uses **PyTorch3D** to create a 3D model of a product from an image, calculating the optimal box size and minimizing void space.
*   **Material Recommendation:** Suggests sustainable packaging alternatives (e.g., "Switch from bubble wrap to mushroom packaging").
*   **Smart Disposal Guides:** Generates QR codes with clear, localized instructions for recycling or composting the packaging.

#### 🛍️ 5. GreenGather AI: Your Personalized AI Green Assistant
GreenGather makes sustainable shopping convenient, affordable, and engaging.
*   **AI Recommendation Engine:** Provides personalized suggestions for eco-friendly products based on user behavior and carbon impact.
*   **Group Buying:** Clusters orders by location to reduce delivery emissions and offers discounts for participation.
*   **Green Coin Economy:** A rewards system where users earn "Green Coins" for making sustainable choices, redeemable for discounts on future purchases.

---


## ⚡ System Architecture

GreenX is built on a modern, scalable, and decoupled architecture. The frontend (React) communicates with a backend (Python) via a Flask, which orchestrates the various AI/ML and Blockchain services and AWS supported element.

-   **Frontend:** A responsive React application provides a seamless user interface for all GreenX features.
-   **Backend API Gateway:** A central Python (Flask/FastAPI) application that serves as the brain, routing requests to the appropriate micro-service or AI model.
-   **AI/ML Services:** Each AI module (EcoSense, CarbonKarma, etc.) is a specialized service, allowing for independent scaling and updates.
-   **Data Layer:** A hybrid data storage approach using SQL for structured data and AWS S3, KMS for unstructured data like images and documents.
-   **Blockchain Network:** An Ethereum-based network for managing the EcoChain Trace certifications and GreenScore™.
![flow1_re](https://github.com/user-attachments/assets/0e0770ae-4bcb-42e0-9309-2020bc0e6b92)

### 🤖 Personalized AI Recommendations: Smarter, Greener, and Hyper-Relevant

GreenX combines **Generative LLMs, reinforcement learning, multi-armed bandits, and graph-based ranking** to deliver cutting-edge, real-time recommendations tailored for sustainability-conscious shoppers.

- 🛒 Suggests **eco-friendly alternatives** to frequently browsed or purchased items.
- 🌿 Calculates and displays the **environmental impact per product** (via **CarbonKarma AI**) — helping users make smarter, low-carbon decisions.
- 📦 Optimizes delivery options through **GreenGather AI**, grouping shipments to reduce packaging waste and emissions.
- 🧠 Learns from your purchase behavior, location, and sustainability preferences to **refine suggestions over time**.

> Every product you see isn’t just relevant — it’s responsible. GreenX makes sustainable shopping **frictionless, intelligent, and personal.**

![recommen](https://github.com/user-attachments/assets/15470bb6-df2e-4b90-a36d-9594e11567ad)


### 🛍️ Seller Registration and Verification System: Trust Built with AI

To ensure only genuine eco-friendly products reach customers, GreenX introduces **EcoSense AI** — a robust, AI-driven seller verification and onboarding system.

- 🔐 Uses **image recognition**, **NSDL/UIDAI APIs**, and **PhotoDNA** to verify authenticity.
- 📍 Detects seller location and maps the **shortest, most efficient route** to Amazon servers using **Dijkstra’s algorithm** — reducing latency and logistics impact.
- 🧾 Enables **paperless registration** for small/local sellers, cutting down bureaucratic friction.
- 🔒 Implements **AES-256 encryption** and **Role-Based Access Control (RBAC)** to ensure **data privacy and security**.

> With EcoSense AI, we eliminate fraud, empower local artisans, and unlock a trusted marketplace for truly sustainable products.

![SellerVerification](https://github.com/user-attachments/assets/3e285439-f68c-42e9-81dc-e2b99a24fb12)

### 🔗 Product Verification & Eco-Listing: Powered by EcoChain Trace (Blockchain)

GreenX brings **transparency and trust** to sustainable shopping with **EcoChain Trace** — a blockchain-based product certification and grading system.

- 🧾 Every product is assigned a **GreenScore™ (A++ to D)** based on **8 sustainability metrics**:
  - ♻️ Recyclability
  - 📦 Packaging Used
  - ⚡ Energy Efficiency
  - 🌿 Materials Used
  - 🏭 Manufacturing Practices
  - 🌍 Carbon Emissions
  - 📜 Eco Certifications
  - 🔁 Product Lifespan
- 🔐 Immutable blockchain ledger ensures **tamper-proof verification** of product origin, composition, and supply chain.
- 🏷️ GreenScore badges and certificates are **visible to users at listing level**, making sustainability claims verifiable and actionable.
- 🛠️ Enables sellers to improve product grading via transparent feedback and analytics.

> With EcoChain Trace, greenwashing becomes impossible. Only **truly sustainable products** earn visibility, trust, and conversion — certified on-chain.

![ProductVerification](https://github.com/user-attachments/assets/83218e92-35eb-44c2-b638-8dfcb0776ad7)

### 📦 Reuse & Return Engine: Closing the Loop on E-Waste

GreenX transforms Amazon's 40M+ monthly product returns from a waste challenge into a circular opportunity.  
Our **Reuse & Return Engine** empowers users to seamlessly **resell, donate, or recycle** previously purchased items directly within the platform.

- ♻️ **List returns for resale or donation** with one click — reducing warehouse pileup.
- 🧠 AI-backed recommendations help suggest best reuse channels based on item condition and category.
- 🪙 Earn **GreenCoins** for choosing reuse over disposal — incentivizing sustainable behavior.
- 🔄 Helps Amazon shift from linear to **circular commerce**, aligning with global ESG goals.

> What was once a return is now a chance to reduce impact, extend product life, and support circular shopping — all inside your Amazon account.

![return](https://github.com/user-attachments/assets/472c1850-0ef7-4119-8fd2-e2fac9373171)

### 🧠 Advanced AI Grading System: Beyond Labels, Built on Logic

GreenX eliminates greenwashing with a hybrid AI grading engine that blends multi-modal analysis, machine learning, and blockchain verification.

*   **Multi-Modal Intelligence:**
    Analyzes product **images** (packaging, labels), **text** (descriptions, reviews), and **metadata** (supply chain data) using models like **CLIP, YOLOv8, and Gemini**.

*   **GreenScore™ Engine:**
    Grades products from **A++ to D** based on 8 key sustainability metrics. It uses **NLP** to verify claims, detect greenwashing, and employs **ML fallback models** to intelligently infer missing data.

*   **Blockchain Certification:**
    The final `GreenScore™` and its supporting data are recorded on a blockchain ledger, creating a **tamper-proof certificate** for each product. This enables transparent audits and displays a trustworthy badge directly on the product page.



>🌱 **No more greenwashing. No more guesswork. Just transparent, verified, and AI-evaluated eco-grades — shown directly at the point of purchase.**### 🧠 Advanced AI Grading System: Beyond Labels, Built on Logic

![grading](https://github.com/user-attachments/assets/8bb644c1-8cd0-4fec-a294-f4a23fb982de)


---

## 🛠️ Tech Stack & Rationale

We chose each technology for its specific strengths in building a scalable, AI-driven, and secure platform.

| Category      | Technology                               | Rationale                                                                                                                            |
| :------------ | :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend**  | React.js, Tailwind CSS                   | **React** for building a fast, component-based, and dynamic user interface. **Tailwind CSS** for rapid, utility-first styling.         |
| **Backend**   | Python (Flask, FastAPI)                  | **Python** is the industry standard for AI/ML. **Flask/FastAPI** provides a lightweight and high-performance framework for building APIs. |
| **Database**  | MySQL, AWS S3                            | **MySQL** for robust, scalable, and ACID-compliant storage of structured data (users, products). **AWS S3** for durable object storage. |
| **AI/ML**     | PyTorch3D, OpenCV, Transformers, Gemini  | **PyTorch3D** for 3D vision (RePack AI). **OpenCV** for image processing. **Transformers/Gemini** for advanced NLP (CarbonKarma AI). |
| **Cloud/AWS** | Rekognition, KMS, S3                     | **AWS Rekognition** for managed, powerful face comparison. **AWS KMS** for secure key management and encryption. **S3** for object storage. |
| **Blockchain**| Ethereum                                 | **Ethereum** for its robust smart contract capabilities, enabling the creation of our immutable certification and token (Green Coin) system. |
| **DevOps**    | Docker, Git/GitHub                       | **Docker** for containerizing applications, ensuring consistent environments. **Git/GitHub** for version control and collaboration.     |

---

## 📂 Project Structure

The repository is organized into a `backend` (Python/Flask) and a `frontend` (React/Vite) directory, promoting a clean separation of concerns.

```
/
├── backend/
│   ├── Carbon_Karma/         # Carbon footprint estimation module
│   ├── seller_registration_fraud_detection/ # Seller verification module
│   ├── adv_recommendation/   # Recommendation engine
│   ├── return_package/       # Return logistics and monitoring
│   ├── models/               # Shared data models and blockchain logic
│   ├── static/               # Static assets (CSS, JS, images)
│   ├── templates/            # HTML templates
│   ├── app.py                # Main Flask application
│   └── .env                  # Environment variables (API keys, secrets)
│
└── frontend/ (src)
    ├── components/           # Reusable React components
    ├── pages/                # Page-level components (Home, Dashboard, etc.)
    ├── context/              # Global state management
    ├── App.jsx               # Main React app component
    └── main.jsx              # Application entry point
```

## 🚀 Getting Started

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/greenx.git
    cd greenx
    ```

2.  **Setup Backend:**
    ```bash
    cd backend
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    # Create and populate your .env file with the necessary API keys
    python app.py
    ```

3.  **Setup Frontend:**
    ```bash
    cd ../frontend
    npm install
    npm run dev
    ```

4.  Open your browser and navigate to `http://localhost:5173` (or the port specified by Vite).

---

## 👥 Team Members

-   **Bisal Prasad**
-   **Chinmoy Dutta**
-   **Subrata Lodh**

## 🙏 Acknowledgments

-   Data and statistics were compiled from reports by TERI, CPCB India, McKinsey, YouGov, and The Economic Times.
-   Inspiration from leaders in the sustainability space like Loopify and Clarity AI.
-   Built with the power of AWS, PyTorch, and the open-source community.

## 🌍 Vision & Impact

### 🔭 Our Vision

At **GreenX**, we envision a world where **sustainability is not a luxury, but the default** — seamlessly integrated into everyday shopping.  
Our mission is to empower **eco-conscious consumers**, **local green businesses**, and **CSR-driven corporations** through an AI-powered, transparent, and rewarding ecosystem embedded into Amazon's marketplace.

We aim to make **Amazon the global leader in sustainable commerce**, where every purchase is:
- Authenticated through blockchain,
- Optimized with AI,
- And rewarded with real-world impact.

---

### 💥 The Impact We Strive For

#### 🛍️ Greener Shopping Experiences
- ✅ Eliminate greenwashing using **EcoChain Trace** (blockchain certification)
- ✅ Showcase **GreenScore™ badges** for product transparency
- ✅ End-to-end sustainability with **five specialized AIs**

#### 🚚 Sustainable Logistics
- ♻️ Reduce plastic waste and emissions via **RePack AI** and **CarbonKarma AI**
- 📦 Promote **optimized packaging** and **group buying** to reduce delivery waste

#### 🎮 Gamified Behavior Change
- 🪙 Introduce **GreenCoin** rewards for eco-friendly actions
- 🏆 Weekly **leaderboards** and personal **impact dashboards** drive engagement

#### 👨‍🌾 Empowering Small Sellers
- 🔓 Paperless seller onboarding using **EcoSense AI**
- 🛍️ Visibility for local artisans and small green businesses

#### 📈 Scalable Global Impact
- 🌐 Phase 1: India-first rollout on Amazon.in (150M+ users)
- 🚀 Phase 2: Global expansion using AWS and AI APIs
- 🧩 Phase 3: API monetization — GreenX as an industry standard

---

### 🤝 Small Business & B2B Collaboration: Powering the Sustainable Supply Chain

GreenX isn’t just built for consumers — it’s a game-changer for **sustainable brands, small businesses, and enterprise partners** looking to meet modern environmental standards and grow with integrity.

#### 🔍 Supply Chain Traceability for Brands
A sustainable clothing brand (e.g., **Seller A**) verifies the eco-sourcing of raw materials from **Supplier B** using **EcoChain Trace**.  
All transactions and certifications are recorded on-chain, ensuring **transparent audits and traceable supply chains**.

#### 🧠 Sustainability-as-a-Service (SaaS)
**CarbonKarma AI** is available as an API for e-commerce platforms and brands.  
It provides **real-time carbon footprint estimates** per product — supporting **ESG compliance**, CSR goals, and sustainability reporting frameworks.

#### 📦 RePack AI Recommendations for Logistics Optimization
Businesses use **RePack AI** to:
- Analyze product shapes & volumes using 3D vision
- Recommend right-sized packaging
- Reduce emissions across warehousing and last-mile delivery

This results in **lower costs, reduced waste, and greener logistics**.

#### ✅ Green Certification Verification for Small Sellers
GreenX acts as a **green credibility partner** for **local artisans, farmers, and micro-sellers**, allowing them to:
- Verify product claims using **EcoSense AI**
- Receive blockchain-based certification stamps
- Be discovered and trusted by large buyers & global customers

#### 🌍 B2B Carbon Credit Marketplace
GreenX enables businesses to trade carbon offsets using smart contracts:
- **Business A** (with surplus credits from eco practices) can sell verified carbon credits to
- **Business B** (needing offset for emissions)
- Trust, pricing, and traceability ensured via **EcoChain Trace**

> From traceability to certification to carbon offsetting — GreenX makes **sustainability scalable, collaborative, and monetizable** across the B2B landscape.

![B2B](https://github.com/user-attachments/assets/3a406ec7-3834-4575-82d3-bd96c32e9e36)

---

### 📊 Key Metrics & Goals

| Goal                          | Target Value                          |
|------------------------------|---------------------------------------|
| 🌱 CO₂ Reduction              | 100,000+ tons/year                    |
| 📦 Plastic Packaging Cut     | 50% reduction (Phase 1)               |
| 🧑‍🌾 Sustainable Sellers      | 1M+ onboarded within 3 years          |
| 💰 Packaging Cost Savings     | ₹1,200 Cr/year for Amazon             |
| 🔁 Circular Commerce          | 40M+ monthly returns reused/resold    |

---

### 💡 Why GreenX Matters

GreenX isn’t just a sustainability feature — it's a **full-stack solution** that transforms how India and the world shops.  
We are redefining e-commerce with:

- ✅ **AI-first architecture**
- ✅ **Blockchain-backed trust**
- ✅ **Gamified engagement**
- ✅ **Seller empowerment**
- ✅ **Global scalability**

> **From cart to climate action — GreenX is not just a product, it's a movement.**

