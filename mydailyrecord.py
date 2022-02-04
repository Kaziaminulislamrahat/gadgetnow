import scrapy
from bs4 import BeautifulSoup as bs
from items import MdItem

with open('u.txt') as file:
    urllist = file.readlines()
urllist = [x.strip() for x in urllist]

full_name = ['Full Name', 'Full name', 'Full Name9', 'Name', 'Real name', 'Real Name/Full Name']
nick_name = ['Nick/Pet Name', 'Nick Name', 'Nickname',
             'Alias', 'Known as', 'Celebrated Name', 'Nick Name/Celebrated Name',
             'Nick Names', 'Now known as']
birth_place = ['Birth Place']
dob = ['Date Of Birth/Birthday']
age = ['Age/How Old']
height = ['Height/How Tall']
weight = ['Weight']
eye = ['Eye Color']
hair = ['Hair Color']
parents = ['Parents Name']
siblings = ['Siblings']
school = ['School']
college = ['College']
religion = ['Religion']
nationality = ['Nationality']
zodiac = ['Zodiac Sign']
gender = ['Gender']
marital = ['Marital Status']
bfgf = ['Boyfriend', 'Girlfriend']
spouse = ['Wife/Spouse Name', 'Husband/Spouse Name']
kids = ['Kids/Children Name']
profession = ['Profession']
net_worth = ['Net Worth']


class DailySpider(scrapy.Spider):
    name = 'daily'
    start_urls = urllist

    def parse(self, response,):
        items = MdItem()

        def mdicts(listu):
            for x in listu:
                if x in dicts.keys():
                    return dicts[x]

        dicts = {'url': response.url}
        trs = response.css('tr').getall()
        for tr in trs:
            html = bs(tr, 'html.parser')
            html_1 = str(html).replace('<th', '<td').replace('<strong>', '').replace('</strong>', '').replace('</th',
                                                                                                              '</td')

            soup = bs(html_1, 'html.parser')
            tds = soup.findAll('td')
            if len(tds) == 2:
                first_ele = tds[0].text.strip().replace(":", "").encode("utf-8").decode()
                second_ele = tds[1].text.strip().replace(":", "").encode("utf-8").decode()
                dicts[first_ele] = second_ele
        images = response.css(".size-full::attr(data-lazy-src)").getall()
        image_one = images[0]
        image_two = images[1]

        print(dicts)
        items['url'] = response.url
        items['full_name'] = mdicts(full_name)
        items['nick_name'] = mdicts(nick_name)
        items['birth_place'] = mdicts(birth_place)
        items['dob'] = mdicts(dob)
        items['age'] = mdicts(age)
        items['height'] = mdicts(height)
        items['weight'] = mdicts(weight)
        items['eye'] = mdicts(eye)
        items['hair'] = mdicts(hair)
        items['parents'] = mdicts(parents)
        items['siblings'] = mdicts(siblings)
        items['school'] = mdicts(school)
        items['college'] = mdicts(college)
        items['religion'] = mdicts(religion)
        items['nationality'] = mdicts(nationality)
        items['zodiac'] = mdicts(zodiac)
        items['gender'] = mdicts(gender)
        items['marital'] = mdicts(marital)
        items['bfgf'] = mdicts(bfgf)
        items['spouse'] = mdicts(spouse)
        items['kids'] = mdicts(kids)
        items['profession'] = mdicts(profession)
        items['net_worth'] = mdicts(net_worth)
        items['image_one'] = image_one
        items['image_two'] = image_two
        yield items