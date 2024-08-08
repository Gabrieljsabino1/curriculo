from fpdf import FPDF

# Criar uma instância de PDF
pdf = FPDF()

# Adicionar uma página
pdf.add_page()

# Definir a fonte e título
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Gabriel Jorge Sabino - Resume", ln=True, align='C')

pdf.ln(10)  # Quebra de linha

# Definir a fonte para o conteúdo
pdf.set_font("Arial", size=12)

# Conteúdo do currículo
content = """
GABRIEL JORGE SABINO

Tingui, Curitiba - PR | Brazilian, Single, 24 years old

Phone: (41) 99765-6052 / (41) 3357-1513

Email: gabrieljsabino11@icloud.com

OBJECTIVE
To work in the IT Support area as an ERP Implementation Analyst or Junior Front-End Developer.

PROFESSIONAL EXPERIENCE
- Dominio Solar | 02/2023 – 08/2024
  Role: IT Analyst / Front-End Developer
  Area of expertise: Network management, implementation and support for GLPI, access management.
  Responsibilities: 
    - Creation of Procedures, Work Instructions, and Manuals.
    - Configuration of DVRs and cameras using Intelbras and Hikvision technologies.
    - Front-end development using React, React Native, Next.js, TypeScript, and JavaScript.

- Sinn Tecnologia | 2021 - 2023
  Role: Angular Developer
  Area of expertise: Development in Angular / Java Spring MVC

- Qualificar TI e Serviços terceirizados | 2020 - 2021
  Role: Responsible for the administration of internal IT infrastructure, including Data and Voice Networks, Servers, Antivirus, Anti-spam, Emails, Firewall (HP Endian), Databases (Progress 10), ERP, Applications, Licenses, Backups, Printers.
  Area of expertise: Helpdesk N1/N2

- TIM S.A | 2019 - 2020
  Role: Attendant / IT Technical Support
  Area of expertise: Helpdesk N1/N2

- OI S.A | 2018 - 2019
  Role: Customer service representative for clarifying doubts and providing information about products and services.
  Area of expertise: Telemarketing

EDUCATION
- UNINTER Centro Universitario Internacional
  2018 - Currently Studying | Computer Engineering - 10th Semester

CERTIFICATIONS AND COURSES
- NLW Unite – DevOps – RocketSeat Completed 04/2024 - 5 hours
- Logic and Programming Course - RocketSeat Completed in 2022
- Information Technology Course - RocketSeat Completed 06/2022 - 60 hours
- ERP Implementation Consultant Analyst - Udemy Completed 03/2023 - 11 hours
- SAP ERP Expert Training (with ABAP) - Udemy Completed 03/2023 - 5.5 hours
- Learn ERP TOTVS Protheus in practice - Finance - Udemy Completed 04/2023 - 5.5 hours

EXPERIENCE IN:
- Infrastructure: N1, N2, and N3 Support, Windows Server, GLPI, Microsoft Environment, Mikrotik Configuration
- WEB/Android Development: HTML-5, CSS, Angular, React, JavaScript, Figma, React Native, Next.js, TailwindCSS, Sanity, Postman, Azure Environment, Android Studio
- Projects: BPMN, Agile Methodology, Scrum, Kanban
- Databases: SQL, MySQL, SAS, PostgreSQL
- Others: Advanced Office Package, Azure

LANGUAGES
- Advanced English 1
  CCAA Language School
  Studying since June/2021
"""

# Substituir caracteres especiais que podem causar erro
content = content.replace('–', '-').replace('’', "'").replace('‘', "'")

# Adicionar conteúdo ao PDF
pdf.multi_cell(0, 10, content)

# Salvar o PDF
pdf_output_path = "Gabriel_Jorge_Sabino_Resume_EN.pdf"
pdf.output(pdf_output_path)

print(f"PDF criado: {pdf_output_path}")
