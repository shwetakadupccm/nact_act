import imaplib
import os
import email
import pandas as pd
import socket
socket.getaddrinfo('127.0.0.1', 8080)

user = 'vcanshare@gmail.com'
password = 'prashanti123'
host = 'imap.gmail.com'

ag_mail_id = 'info@agdiagnostics.com'
ruby_hall_mail_id = ['labwan@rubyhall.com', 'labreports@rubyhall.com']
jeh_mail_id = ['nutan.jumle@jehangirhospital.com', 'lab@jehangirhospital.com']

mail = imaplib.IMAP4_SSL(host='imap.gmail.com', port=993)
mail.login(user, password)
mail.select('Inbox')
type, data = mail.search(None, '(FROM "info@agdiagnostics.com")')

mail_ids = data[0]
id_list = mail_ids.split()

info1 = []
for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('D:/Shweta/email/trial', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                file_name_subject = [fileName, subject]
                info1.append(file_name_subject)
                print('done')

                # print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName,
                #                                                 subject=subject,
                #                                                 uid=latest_email_uid.decode('utf-8')))


info_df = pd.DataFrame(info, columns=['attachment_name', 'email_subject'])
info1_df = pd.DataFrame(info1, columns=['attachment_name', 'email_subject'])

df = pd.concat([info_df, info1_df], axis=0)


##
def download_email_attachment(username, password, download_attach_from = '', attachments_output_folder_path = ''):
    mail = imaplib.IMAP4_SSL(host='imap.gmail.com', port=993)
    mail.login(username, password)
    mail.select('Inbox')
    info = []
    type, data = mail.search(None, '(FROM ' + '"' + download_attach_from + '"' +')')
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            if bool(fileName):
                filePath = os.path.join(attachments_output_folder_path, fileName)
                if not os.path.isfile(filePath):
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                    subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                    file_name_subject = [fileName, subject]
                    info.append(file_name_subject)
                    print('done')
    df = pd.DataFrame(info, columns=['attchment_name', 'subject'])
    return df

output_df = download_email_attachment(user, password, 'info@agdiagnostics.com', 'D:/Shweta/email/trial')

output_df.to_excel('D:/Shweta/email/attachments_from_ag/folder_info_df/2021_09_08_AG_report_names_subject_sk.xlsx',
                   index=False)

output_df1 = download_email_attachment(user, password, 'labreports@rubyhall.com', 'D:/Shweta/email/trial')

df = pd.concat([output_df, output_df1], axis=0)
df.to_excel('D:/Shweta/email/attachments_from_ruby_hall/folder_info_df/2021_09_08_ruby_hall_report_names_subject_sk.xlsx',
                index=False)

