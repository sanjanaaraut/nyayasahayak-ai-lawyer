# legal_kb.py — Verified Indian Legal Knowledge Base (Anti-Hallucination Grounding)

LEGAL_KB = {
    "Rental Security Deposit": {
        "laws_and_sections": [
            "Indian Contract Act, 1872 (Sections 73 & 74): Recovery is limited to reasonable compensation for actual loss. A landlord cannot automatically forfeit the entire deposit without proof of actual damage or unpaid dues.",
            "Transfer of Property Act, 1882 & State Rent Control Acts: Tenancy rights and notice periods depend on the signed rent agreement and the specific state's tenancy law.",
            "Model Tenancy Act, 2021 (Section 11): Provides for refund of security deposit upon handover of vacant possession after permissible deductions, and proposes a 2-month cap for residential deposits—note that this applies only in states that have adopted it."
        ],
        "what_counts_as_proof": [
            "Signed rent/lease agreement",
            "Bank transfer receipts / UPI / UTR numbers showing deposit payment",
            "Photos/video of the flat condition at move-in and move-out",
            "Key handover confirmation (WhatsApp/email) and cleared utility bills"
        ],
        "step_by_step_options": [
            "1. Send a written demand on WhatsApp/email listing exact dues and move-out proof.",
            "2. Send a formal Legal Notice (by Speed Post / Registered Post AD + email) giving a 15 to 30-day deadline to refund the deposit.",
            "3. If unpaid, file a civil recovery suit (or Rent Authority/Consumer Commission complaint if applicable) — consult a lawyer before filing in court."
        ],
        "when_to_get_real_lawyer": "If the deposit amount is large, the landlord threatens a counter-claim for property damage, or you need to file a formal court recovery suit."
    },
    "Consumer Refund / Defective Service": {
        "laws_and_sections": [
            "Consumer Protection Act, 2019 (Section 2(7)): Protects anyone who buys goods or hires services for personal use (not resale/commercial) against deficiency in service or unfair trade practices.",
            "Section 69 (Time Limit): Complaints must generally be filed within 2 years from the date the issue occurred.",
            "Filing Fee: Nil (₹0) court fee for complaints where the value paid is up to ₹5 lakh."
        ],
        "what_counts_as_proof": [
            "Invoice, order confirmation, or payment receipt",
            "Screenshots of refund policy, chats, or support ticket numbers",
            "Photos/videos of damaged or non-working product"
        ],
        "step_by_step_options": [
            "1. File a grievance with the company's Grievance Officer in writing (email).",
            "2. Register on the National Consumer Helpline (call toll-free 1915 or file at consumerhelpline.gov.in) for free pre-litigation mediation.",
            "3. If unresolved, file an online consumer case yourself (no lawyer mandatory) on e-Jagriti (e-jagriti.gov.in, which replaced e-Daakhil on Jan 1, 2025)."
        ],
        "when_to_get_real_lawyer": "If the claim is above ₹50 lakh (State/National Commission) or involves complex medical/builder disputes."
    },
    "Unpaid Salary": {
        "laws_and_sections": [
            "Payment of Wages Act, 1936 (Sections 4 & 15): Applies to employees within the statutory wage bracket—wages must be paid monthly (by the 7th/10th of the next month) and within 2 days upon termination.",
            "Indian Contract Act, 1872: For employees earning above the Payment of Wages Act threshold, the signed employment contract governs salary recovery as a civil breach of contract."
        ],
        "what_counts_as_proof": [
            "Offer letter / employment contract and salary slips",
            "Bank statements showing past salary credits and missing months",
            "Emails/WhatsApp messages asking HR/management for pending salary",
            "Relieving letter or attendance/work logs"
        ],
        "step_by_step_options": [
            "1. Send a formal written demand email to HR/management citing exact unpaid months and amount.",
            "2. Send a formal Legal Notice via Speed Post/email giving 15 days to clear dues.",
            "3. File a complaint with the local Assistant/District Labour Commissioner (if covered under labour laws) or pursue a civil recovery suit under the Contract Act."
        ],
        "when_to_get_real_lawyer": "If you are in a managerial/high-salary role outside Labour Commissioner jurisdiction, or if the company is shutting down/insolvent."
    }
}

OUT_OF_SCOPE_NOTICE = (
    "I am an AI assistant scoped ONLY to everyday Indian disputes around "
    "Rental Security Deposits, Consumer Refunds, and Unpaid Salary. "
    "I cannot advise on criminal cases, divorce/family law, property title disputes, "
    "or tax/corporate litigation. Please consult a qualified advocate for those matters."
)