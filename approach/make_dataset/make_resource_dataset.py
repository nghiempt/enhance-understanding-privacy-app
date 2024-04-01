import pandas as pd
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen

class DATASET_MAKER:

    @staticmethod
    def load_html_content(url):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        return soup
    
    @staticmethod
    def findAppName(soup):
        appName = soup.find('h1', class_='Fd93Bb').get_text()
        return appName
    
    @staticmethod
    def findDeveloper(soup):
        developer = soup.find('div', class_='Vbfug').get_text()
        return developer
    
    @staticmethod
    def findCategory(soup):
        container = soup.find('div', class_='Uc6QCc')
        tags = container.findAll('span', class_='VfPpkd-vQzf8d')
        content = ''
        idx = 0
        for tag in tags:
            if tag.get_text().startswith("#"):
                continue
            if idx < len(tags) - 2:
                content = content + tag.get_text() + '+'
            else:
                content = content + tag.get_text()
            idx = idx + 1
        return content
    
    @staticmethod
    def findNumberOfDownload(soup):
        numberOfDownload = soup.findAll('div', class_='ClM7O')
        numberOfDownloadText = numberOfDownload[1].get_text()
        if numberOfDownloadText == '':
            numberOfDownloadText = numberOfDownload[0].get_text()
        return numberOfDownloadText
    
    @staticmethod
    def findPrivacyPolicyLink(soup):
        pp_link = ""
        try:
            container = soup.findAll('div', class_='VfPpkd-WsjYwc')
            container = container[-1]
            pp_link = container.find('a', class_='Si6A0c')['href']
        except Exception:
            print("Error at finding privacy policy link")
        return pp_link
    
    @staticmethod
    def generate_dataset(package_name: str, id):
        print(f"Generating dataset for package: {package_name}")
        try:
            soup = DATASET_MAKER.load_html_content("https://play.google.com/store/apps/details?id=" + row['package_name'])
        except:
            print("error")
            return
            
        appName = DATASET_MAKER.findAppName(soup)
        developer = DATASET_MAKER.findDeveloper(soup)
        numberOfDownload = DATASET_MAKER.findNumberOfDownload(soup)
        categories = DATASET_MAKER.findCategory(soup)
        pp_link = DATASET_MAKER.findPrivacyPolicyLink(soup)
        new_row = [str(id), appName, package_name, "14-10-2023", developer, categories, numberOfDownload, "https://play.google.com/store/apps/datasafety?id=" + package_name, pp_link]
        print(str(new_row))
        return new_row

if __name__ == "__main__":
    df = pd.read_csv('')

    new_data = []
    new_columns = ['id', 'app_name', 'package_name', 'date_of_analysis', 'developer', 'category', 'number_of_downloads', 'data_safety_link', 'privacy_policy_link']

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        print("========== " + str(index + 1) + " times ==========")
        new_row = DATASET_MAKER.generate_dataset(row['package_name'], row['id'])
        new_data.append(new_row)

    new_df = pd.DataFrame(new_data, columns=new_columns)

    new_df.to_csv("", index=False)
