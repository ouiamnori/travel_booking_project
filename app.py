from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Book route to display the booking form and handle submission
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        destination = request.form['destination']
        dates = request.form['dates']
        guests = request.form['guests']
        budget = request.form['budget']
        
        # Render the confirmation page with the submitted data
        return render_template('confirmation.html', destination=destination, dates=dates, guests=guests, budget=budget)

    return render_template('book.html')

# Contact route to handle the contact form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send the email
        send_email(name, email, message)

        # After submitting, show the contact confirmation page
        return render_template('contact_confirmation.html', name=name)

    return render_template('contact.html')

# Function to handle email sending for contact form
def send_email(name, email, message):
    try:
        # Set up the SMTP server (example with Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your-email@gmail.com", "your-email-password")  # Replace with your credentials

        # Format the email message
        subject = f"Message from {name}"
        body = f"From: {name} <{email}>\nMessage: {message}"
        msg = f"Subject: {subject}\n\n{body}"

        # Send email (replace recipient's email)
        server.sendmail("your-email@gmail.com", "recipient-email@gmail.com", msg)
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
