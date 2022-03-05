import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

import os

load_dotenv()


async def send_code(receiver, code):
    mail_content ="""<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
   <head>
      <title>New login attempt on Android in Inspi Guard System</title>
      <!--[if !mso]><!-->
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <!--<![endif]-->
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <style type="text/css">#outlook a { padding:0; }
         body { margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%; }
         table, td { border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt; }
         img { border:0;height:auto;line-height:100%; outline:none;text-decoration:none;-ms-interpolation-mode:bicubic; }
         p { display:block;margin:13px 0; }
      </style>
      <!--[if mso]>
      <noscript>
         <xml>
            <o:OfficeDocumentSettings>
               <o:AllowPNG/>
               <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
         </xml>
      </noscript>
      <![endif]--><!--[if lte mso 11]>
      <style type="text/css">
         .mj-outlook-group-fix { width:100% !important; }
      </style>
      <![endif]--><!--[if !mso]><!-->
      <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
      <style type="text/css">@import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);</style>
      <!--<![endif]-->
      <style type="text/css">@media only screen and (min-width:480px) {
         .mj-column-per-100 { width:100% !important; max-width: 100%; }
         }
      </style>
      <style media="screen and (min-width:480px)">.moz-text-html .mj-column-per-100 { width:100% !important; max-width: 100%; }</style>
      <style type="text/css">@media only screen and (max-width:480px) {
         table.mj-full-width-mobile { width: 100% !important; }
         td.mj-full-width-mobile { width: auto !important; }
         }
      </style>
      <style type="text/css">.ltr div {
         direction: ltr !important;
         }
         .ltr td {
         direction: ltr !important;
         }
         .rtl div {
         direction: rtl !important;
         }
         .rtl td {
         direction: rtl !important;
         }
      </style>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
   </head>
   <body style="word-spacing:normal;">
      <div class="body" style="max-width: 310px; margin: 0px auto;">
         <!--[if mso | IE]>
         <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:600px;" width="600" >
            <tr>
               <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                  <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                           <tr>
                              <td style="direction: ltr; font-size: 0px; text-align: center; padding: 0px;" align="center">
                                 <!--[if mso | IE]>
                                 <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                       <td class="" style="vertical-align:top;width:600px;" >
                                          <![endif]-->
                                          <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                             <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                                <tbody>
                                                   <tr>
                                                      <td align="center" class="fxa-logo" style="font-size: 0px; word-break: break-word; padding: 20px 0px; height: 60px; margin: 0 auto; display: block;" height="60">
                                                         <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                                            <tbody>
                                                               <tr>
                                                               </tr>
                                                            </tbody>
                                                         </table>
                                                      </td>
                                                   </tr>
                                                </tbody>
                                             </table>
                                          </div>
                                          <!--[if mso | IE]>
                                       </td>
                                    </tr>
                                 </table>
                                 <![endif]-->
                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </div>
                  <!--[if mso | IE]>
               </td>
            </tr>
         </table>
         <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:600px;" width="600" >
            <tr>
               <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                  <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                           <tr>
                              <td style="direction: ltr; font-size: 0px; text-align: center; padding: 0px;" align="center">
                                 <!--[if mso | IE]>
                                 <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                       <td class="" style="vertical-align:top;width:600px;" >
                                          <![endif]-->
                                          <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                             <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                                <tbody>
                                                   <tr>
                                                      <td align="left" class="text-header" style="font-size: 0px; word-break: break-word; padding: 0px;">
                                                         <div style="color: #000000; font-size: 20px; line-height: 28px; font-family: sans-serif; margin-bottom: 12px; text-align: center;"><span data-l10n-id="newDeviceLogin-title" data-l10n-args="{&quot;clientName&quot;:&quot;Firefox for Android&quot;}">New login attempt on Android in Inspi Guard System! <br> Use this code for auth in our app!</span></div>
                                                      </td>
                                                   </tr>
                                                </tbody>
                                             </table>
                                          </div>
                                          <!--[if mso | IE]>
                                       </td>
                                    </tr>
                                 </table>
                                 <![endif]-->
                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </div>
                  <!--[if mso | IE]>
               </td>
            </tr>
         </table>
         <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:600px;" width="600" >
            <tr>
               <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                  <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                           <tr>
                              <td style="direction: ltr; font-size: 0px; text-align: center; padding: 0px;" align="center">
                                 <!--[if mso | IE]>
                                 <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                       <td class="" style="vertical-align:top;width:600px;" >
                                          <![endif]-->
                                          <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                             <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                             </table>
                                          </div>
                                          <!--[if mso | IE]>
                                       </td>
                                    </tr>
                                 </table>
                                 <![endif]-->
                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </div>
                  <!--[if mso | IE]>
               </td>
            </tr>
         </table>
         <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:600px;" width="600" >
            <tr>
               <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                  <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                           <tr>
                              <td style="direction: ltr; font-size: 0px; text-align: center; padding: 0px;" align="center">
                                 <!--[if mso | IE]>
                                 <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                       <td class="" style="vertical-align:top;width:600px;" >
                                          <![endif]-->
                                          <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                             <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                                <tbody>
                                                   <tr>
                                                      <td align="center" vertical-align="middle" class="primary-button" style="font-size: 0px; word-break: break-word; padding: 0px; height: 56px; width: 310px;" width="310" height="56">
                                                         <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                                                            <tbody>
                                                               <tr>
                                                                  <td align="center" bgcolor="#414141" role="presentation" style="border: none; border-radius: 3px; cursor: auto; mso-padding-alt: 10px 25px; background: #414141; padding: 0px;" valign="middle"><a href="" disabled style="display: inline-block; color: #ffffff; font-weight: normal; margin: 0; text-decoration: none; text-transform: none; mso-padding-alt: 0px; font-size: 18px; line-height: 28px; font-family: sans-serif; background: #0090ed; width: 310px; padding: 16px 0px; border-radius: 4px;" target="_blank"><span data-l10n-id="newDeviceLogin-action">""" + str(code) + """</span></a></td>
                                                               </tr>
                                                            </tbody>
                                                         </table>
                                                      </td>
                                                   </tr>
                                                </tbody>
                                             </table>
                                          </div>
                                          <!--[if mso | IE]>
                                       </td>
                                    </tr>
                                 </table>
                                 <![endif]-->
                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </div>
                  <!--[if mso | IE]>
               </td>
            </tr>
         </table>
         <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:600px;" width="600" >
            <tr>
               <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                  <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                           <tr>
                              <td style="direction: ltr; font-size: 0px; text-align: center; padding: 0px;" align="center">
                                 <!--[if mso | IE]>
                                 <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                       <td class="" style="vertical-align:top;width:600px;" >
                                          <![endif]-->
                                          <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                             <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                                <tbody>
                                                   <tr>
                                                      <td align="left" class="text-footer-automatedEmail" style="font-size: 0px; word-break: break-word; padding: 0px;">
                           
                                                      </td>
                                                   </tr>
                                                </tbody>
                                             </table>
                                          </div>
                                          <!--[if mso | IE]>
                                       </td>
                                    </tr>
                                 </table>
                                 <![endif]-->
                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </div>
                  <!--[if mso | IE]>
               </td>
            </tr>
         </table>
         <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:600px;" width="600" >
            <tr>
               <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                  <![endif]-->
                  <div style="margin:0px auto;max-width:600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                           <tr>
                              <td style="direction: ltr; font-size: 0px; text-align: center; padding: 0px;" align="center">
                                 <!--[if mso | IE]>
                                 <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                    <tr>
                                       <td class="" style="vertical-align:top;width:600px;" >
                                          <![endif]-->
                                          <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                             
                                          </div>
                                          <!--[if mso | IE]>
                                       </td>
                                    </tr>
                                 </table>
                                 <![endif]-->
                              </td>
                           </tr>
                        </tbody>
                     </table>
                  </div>
                  <!--[if mso | IE]>
               </td>
            </tr>
         </table>
         <![endif]-->
      </div>
   </body>
</html>
"""

    sender_email = "inspishares@gmail.com"
    receiver_email = receiver
    password = os.getenv("emailpass")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Inspi Guard System - Verification code"
    message["From"] = sender_email
    message["To"] = receiver_email


    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(mail_content, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )