import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailClientApp:
    def __init__(self, master):
        self.master = master
        master.title("Email Client")

        self.server_label = tk.Label(master, text="Server:")
        self.server_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.server_entry = tk.Entry(master, width=30)
        self.server_entry.grid(row=0, column=1, padx=10, pady=5)

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.username_entry = tk.Entry(master, width=30)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.password_entry = tk.Entry(master, show="*", width=30)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        self.to_label = tk.Label(master, text="To:")
        self.to_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.to_entry = tk.Entry(master, width=30)
        self.to_entry.grid(row=3, column=1, padx=10, pady=5)

        self.subject_label = tk.Label(master, text="Subject:")
        self.subject_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        self.subject_entry = tk.Entry(master, width=30)
        self.subject_entry.grid(row=4, column=1, padx=10, pady=5)

        self.message_label = tk.Label(master, text="Message:")
        self.message_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

        self.message_text = tk.Text(master, height=5, width=30)
        self.message_text.grid(row=5, column=1, padx=10, pady=5)

        self.send_button = ttk.Button(master, text="Send", command=self.send_email)
        self.send_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.receive_button = ttk.Button(master, text="Receive", command=self.receive_emails)
        self.receive_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def send_email(self):
        server = self.server_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        to = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        try:
            # Connect to SMTP server
            smtp_server = smtplib.SMTP(server)
            smtp_server.starttls()
            smtp_server.login(username, password)

            # Compose email
            msg = MIMEMultipart()
            msg['From'] = username
            msg['To'] = to
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Send email
            smtp_server.send_message(msg)

            # Close SMTP connection
            smtp_server.quit()

            messagebox.showinfo("Success", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")

    def receive_emails(self):
        server = self.server_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            # Connect to IMAP server
            imap_server = imaplib.IMAP4_SSL(server)
            imap_server.login(username, password)
            imap_server.select('inbox')

            # Search for emails
            typ, data = imap_server.search(None, 'ALL')

            emails = []
            for num in data[0].split():
                typ, msg_data = imap_server.fetch(num, '(RFC822)')
                raw_email = msg_data[0][1]
                email_message = email.message_from_bytes(raw_email)
                emails.append({
                    'From': email_message['From'],
                    'Subject': email_message['Subject'],
                    'Date': email_message['Date']
                })

            # Display received emails
            messagebox.showinfo("Received Emails", "\n".join([f"From: {email['From']}\nSubject: {email['Subject']}\nDate: {email['Date']}\n" for email in emails]))

            # Close IMAP connection
            imap_server.close()
            imap_server.logout()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to receive emails: {str(e)}")

def main():
    root = tk.Tk()
    app = EmailClientApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
