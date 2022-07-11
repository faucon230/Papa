import email, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.utils import timezone





def sendMail3(request):
    prenom = request.POST.get("prenom_demandeur", "")
    nom = request.POST.get("nom_demandeur", "")
    mail = request.POST.get("mail", "")
    nomMachine = request.POST.get("nom_de_la_machine", "")
    url = request.POST.get("url", "")
    os = request.POST.get("version_os", "")
    vpn = request.POST.get("vpn", "")
    TCP = request.POST.get("ports_tcp_ext", "")
    UDP = request.POST.get("ports_udp_ext", "")
    coeurs = request.POST.get("nombre_de_coeurs", "")
    ram = request.POST.get("ram", "")
    HDD = request.POST.get("alloc_HDD", "")
    SSD = request.POST.get("alloc_SSD", "")
    autre = request.POST.get("autre", "")
    utilisation = request.POST.get("utilisation", "")
    date_debut = request.POST.get("date_début", "")
    date_fin = request.POST.get("date_fin", "")

    subject = "Demande VM : "+nomMachine

    body = "Formulaire : demande de création de machine virtuelle \n"
    body+= "Demande faite à " + str(timezone.now) + "\n"
    body+="demandeur : " + prenom + " " + nom + ", adresse mail : " + mail + "\n"
    body+="nom de la machine : " + nomMachine + ", url : " + url + "\n"
    body+="OS de la machine : " + os + "\n"
    body+="connexion VPN : " + vpn + "\n"
    body+="port TCP : " + TCP + ", port UCP : " + UDP + "\n"
    body+="nombre de coeurs : " + coeurs + ", RAM : " + ram + "\n"
    body+="HDD : " + HDD + ", SSD : " + SSD + "\n"
    body+="utilisation de la machine : " + utilisation + "\n"
    body+="remarque : " + autre + "\n"
    body+="début : " + date_debut + ", date de fin : " + date_fin + "\n"


    sender_email = "enseademandevm@gmail.com"
    receiver_email = "enseademandevm@gmail.com"
    password = "zylnrddcgruayrfh"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    return
