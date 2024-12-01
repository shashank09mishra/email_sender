from flask import Flask, render_template, request, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'secret_key'  # Required for flashing messages (error/success)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        # Retrieve form data
        from_email = request.form.get('from_email')
        to_email = request.form.get('to_email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # SMTP Configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        username = "your_real_email@gmail.com"  # Replace with your real email
        password = "your_real_password"         # Replace with your real password or app password if 2FA is enabled

        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Send email via SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(username, password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()

            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email: {str(e)}', 'danger')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
