
# Amazon GreenX: The AI Hub for Sustainable Shopping

**Team-0101**: Bisal Prasad | Chinmoy Dutta | Subrata Lodh

![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Platform](https://img.shields.io/badge/Platform-AWS%20%7C%20React%20%7C%20Python-orange)

GreenX is a full-stack AI and Blockchain ecosystem integrated into Amazon to solve the critical challenges of sustainable e-commerce. It transforms the shopping experience by providing verifiable trust, intelligent waste reduction, and powerful incentives for both consumers and sellers.

---

## 🚩 The Problem: The Paradox of Sustainable Shopping

Despite growing eco-consciousness, consumers and businesses are trapped in a cycle of distrust, waste, and inaction.

1.  **The Greenwashing Fog:** "Eco-friendly" claims are rampant and unreliable. With **78% of green labels on Indian e-commerce being unverified** (TERI, 2024), consumers have no way to identify genuinely sustainable products, leading to widespread distrust.

2.  **The Plastic Default:** Inefficient packaging is the norm. **72% of Amazon India shipments use plastic**, contributing to an estimated **11,000 tons of plastic waste annually** (CPCB, 2024). This is not only an environmental disaster but also a massive operational inefficiency.

3.  **The Motivation Gap:** The path of least resistance is linear consumption. With over **40 million monthly returns** and **less than 5% of consumers engaging in recycling programs**, there is a clear lack of incentive. **84% of shoppers refuse to pay a premium** for sustainability without tangible rewards (BCG).

This isn't just an environmental issue; it's a **$30 billion market opportunity** in India alone (IBEF, 2027) waiting for a scalable, trustworthy solution.

## 💡 The Solution: Amazon GreenX

GreenX is a suite of five specialized AI and Blockchain modules that work in concert to create a transparent, efficient, and rewarding sustainable marketplace. It's not a single monolithic AI; it's a precise, modular ecosystem built for scale and accuracy.

### Key Features

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
![flow1_re](https://github.com/user-attachments/assets/0e0770ae-4bcb-42e0-9309-2020bc0e6b92)

## 🏛️ System Architecture

GreenX is built on a modern, scalable, and decoupled architecture. The frontend (React) communicates with a backend (Python) via a REST API, which orchestrates the various AI/ML and Blockchain services.

-   **Frontend:** A responsive React application provides a seamless user interface for all GreenX features.
-   **Backend API Gateway:** A central Python (Flask/FastAPI) application that serves as the brain, routing requests to the appropriate micro-service or AI model.
-   **AI/ML Services:** Each AI module (EcoSense, CarbonKarma, etc.) is a specialized service, allowing for independent scaling and updates.
-   **Data Layer:** A hybrid data storage approach using SQL for structured data and AWS S3 for unstructured data like images and documents.
-   **Blockchain Network:** An Ethereum-based network for managing the EcoChain Trace certifications and GreenScore™.

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

