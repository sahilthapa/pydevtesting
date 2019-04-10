import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt


hy_issuer_names = ['TURKEY', 'EGYPT', 'ESKOM', 'BHRAIN', 'LEBAN', 'ISCTR', 'KENINT', 'NGERIA', 'PKSTAN']

#smtphub.uk.mail.db.com

def classify_risk():
    risk_data = pd.read_csv('E:/Personal Directories/Sahil/pnl reports/Test_9Apr_py.csv', encoding='ISO-8859-1')
    risk_data['Category'] = 'IG'
    for y in hy_issuer_names:
        risk_data.loc[risk_data['Security'].str.startswith(y), 'Category'] = 'HY'

    output_df1 = risk_data.groupby(['Category', 'Cntry(s)']).agg({'CR01':'sum'}).reset_index()
    output_df2 = risk_data.groupby(['Category']).agg({'CR01': 'sum'}).reset_index()
    output_df1['CR01'] = output_df1['CR01'].map('{:,.0f}'.format)
    output_df2['CR01'] = output_df2['CR01'].map('{:,.0f}'.format)
    #print ( output_df1, output_df2)
    #output_df1.plot(kind='bar')
    #output_df2.plot(kind='bar')
    #plt.show()
    #print (output_df2)
    #output_df1.hist(column = 'CR01')
    send_email(output_df2.sort(['Category', 'CR01']).to_html(index=False)
              + '<br><br>' + output_df1.sort(['Category', 'CR01']).to_html(index=False))


def draw_plots(data):
    # plt.style.use(['bmh'])
    fig, ax = plt.subplots(1)
    fig.suptitle("BreakDown", fontsize=16)
    ax.set_xlabel('Category')
    ax.set_ylabel('Risk')
    #x_axis = numpy.arange(0, len(processes[0]), 1)
    #for i in range(len(processes)):
    #    plt.plot(x_axis, processes[i])
    #plt.show()

def send_email(df):
    server = smtplib.SMTP('smtphub.uk.mail.ss.com')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'IG / HY Classified Risk'
    msg['From'] = 'sahil.thapa@db.com'
    msg['To'] = 'sahil.thapa@db.com'
    #msg.attach(MIMEText(messagePlain, 'plain'))
    msg.attach(MIMEText(df, 'html'))
    server.sendmail('sahil.thapa@db.com','sahil.thapa@db.com', msg.as_string())
    server.quit()


if __name__ == "__main__":
    #send_email()
    classify_risk()
