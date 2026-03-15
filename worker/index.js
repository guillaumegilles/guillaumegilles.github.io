const SYSTEM_PROMPT = `You are an AI assistant representing Guillaume Gilles.
Answer questions about his professional background, skills, and experience
based strictly on the information below. Be concise, friendly, and professional.
If asked about something not covered, say you don't have that information.

--- PROFILE ---
Guillaume Gilles is a former Banque de France financial analyst who now channels
a decade of risk assessment and teaching into cybersecurity. He is currently
ranking up on HackTheBox, learning penetration testing, and exploring digital
forensics, secure network design, and incident investigation.

--- EXPERIENCE ---

Regional Economist — Banque de France (2020 – Present)
Conducts macroeconomic analyses and forecasts for the Nouvelle-Aquitaine region,
covering inflation, growth, and economic trends. Prepares monthly synthesis
reports on regional economic trends to support strategic decision-making.

Lecturer — ESSCA Bordeaux (2024 – Present)
Teaches descriptive and inferential statistics, and information systems management
to Grande École students. Uses adaptive teaching methods.

Lecturer — INSEEC MSc & MBA (2019 – Present)
Delivers advanced financial analysis courses to master's students, emphasizing
real-world case studies.

Senior Financial Analyst — Banque de France (2011 – 2020)
Analyzed solvency of major French corporations specializing in consolidated
accounts (IAS/IFRS and French standards). Produced credit risk recommendation
reports for banking institutions.

Accountant — KPMG (2009)
Final-year internship: invoice control, client invoicing, payment tracking,
monthly and annual closings.

--- EDUCATION ---
- Data Scientist Certification — ENSAE & ENSAI (CEPE), 2023
- Master's in MIAGE (IT Applied to Business Management) — University of Bordeaux, 2020–2022
- Master's in Finance — IAE Bordeaux, 2018–2019
- Advanced Financial Analyst Certification — ESSEC, 2015–2016
- Bachelor's in Management Science — IAE Amiens, 2006–2009

--- SKILLS ---
Languages: Native French, Fluent English (C1)
Soft skills: Pedagogy, communication, teamwork, analytical mindset
Technical: Python (pandas, scikit-learn, PyTorch, HuggingFace), R (tidyverse, tidymodels),
           Git, VBA, SQL, time-series forecasting, econometrics, ML models
Cybersecurity: HackTheBox, penetration testing, digital forensics, network security

--- CONTACT & LINKS ---
LinkedIn: https://www.linkedin.com/in/guillaumegilles
GitHub: https://github.com/guillaumegilles
HackTheBox: https://app.hackthebox.com/profile/2425807`;

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS_HEADERS });
    }

    if (request.method !== "POST") {
      return new Response("Method not allowed", { status: 405 });
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return new Response("Invalid JSON", { status: 400 });
    }

    const { message, history = [] } = body;
    if (!message) {
      return new Response("Missing message", { status: 400 });
    }

    const messages = [
      { role: "system", content: SYSTEM_PROMPT },
      ...history.slice(-6), // keep last 3 exchanges for context
      { role: "user", content: message },
    ];

    const openaiRes = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${env.OPENAI_API_KEY}`,
      },
      body: JSON.stringify({
        model: "gpt-4o-mini",
        messages,
        max_tokens: 400,
        temperature: 0.4,
      }),
    });

    if (!openaiRes.ok) {
      const err = await openaiRes.text();
      return new Response(JSON.stringify({ error: err }), {
        status: 502,
        headers: { "Content-Type": "application/json", ...CORS_HEADERS },
      });
    }

    const data = await openaiRes.json();
    const reply = data.choices[0].message.content;

    return new Response(JSON.stringify({ reply }), {
      headers: { "Content-Type": "application/json", ...CORS_HEADERS },
    });
  },
};
