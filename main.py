import feedparser, time

URL = "https://kimseoyeon23.github.io/feed."
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
<div align="center">

![header](https://capsule-render.vercel.app/api?type=Cylinder&height=200&text=Welecome&fontAlign=50&color=random&customColorList=0,2,2,5,30&animation=fadeIn&desc=SeoYeon's%20Profile&descSize=25&descAlign=56&descAlignY=75)

# Stack📚
<br/>
<h3> 📲 Back-end Stack 📲 </h3>
<img alt="Laravel" src="https://img.shields.io/badge/Laravel-FF2D20.svg?style=for-the-badge&logo=Laravel&logoColor=white"/>
<img alt="Node.js" src="https://img.shields.io/badge/Node.js-339933.svg?style=for-the-badge&logo=Laravel&logoColor=white"/>
<br/>
<br/>
<h3>💻 Front-end Stack 💻 <h3/>
<img alt="HTML" src="https://img.shields.io/badge/HTML-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white"/>
<img alt="CSS3" src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white"/>
<img alt="Javascript" src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=white"/>
<img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white"/>
<br/>
<img alt="React" src="https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=white"/>
<img alt="Next.js" src="https://img.shields.io/badge/Next.js-000000.svg?style=for-the-badge&logo=Next.js&logoColor=white"/>
<img alt="Laravel" src="https://img.shields.io/badge/Laravel-FF2D20.svg?style=for-the-badge&logo=Laravel&logoColor=white"/>
<img alt="Chakra UI" src="https://img.shields.io/badge/Chakra UI-319795.svg?style=for-the-badge&logo=Chakra UI&logoColor=white"/>
<img alt="Tailwind CSS" src="https://img.shields.io/badge/Tailwind CSS-06B6D4.svg?style=for-the-badge&logo=Tailwind CSS&logoColor=white"/>
<br/>
<br/>
<h3>📫 DataBase Stack 📫 <h3/>
<img alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1.svg?style=for-the-badge&logo=MySQL&logoColor=white"/>
<br/>
<br/>
<h3> 💾 Etc Stack 💾 <h3/>
<img alt="npm" src="https://img.shields.io/badge/npm-CB3837.svg?style=for-the-badge&logo=npm&logoColor=white"/>
<img alt="Yarn" src="https://img.shields.io/badge/Yarn-2C8EBB.svg?style=for-the-badge&logo=Yarn&logoColor=white"/>
<br/>
<br/>
<h3> 📝 Tools 📝 <h3/>
<img alt="VisualStudioCode" src="https://img.shields.io/badge/VisualStudioCode-007ACC.svg?style=for-the-badge&logo=VisualStudioCode&logoColor=white"/>
<img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white"/>
<img alt="GitLab" src="https://img.shields.io/badge/GitLab-FC6D26.svg?style=for-the-badge&logo=GitLab&logoColor=white"/>
<img alt="IPFS" src="https://img.shields.io/badge/IPFS-65C2CB.svg?style=for-the-badge&logo=IPFS&logoColor=white"/>
<br/>
<img alt="Slack" src="https://img.shields.io/badge/Slack-4A154B.svg?style=for-the-badge&logo=Slack&logoColor=white"/>
<img alt="Notion" src="https://img.shields.io/badge/Notion-000000.svg?style=for-the-badge&logo=Notion&logoColor=white"/>
<img alt="Jira" src="https://img.shields.io/badge/Jira-0052CC.svg?style=for-the-badge&logo=Jira&logoColor=white"/>
<img alt="Confluence" src="https://img.shields.io/badge/Confluence-172B4D.svg?style=for-the-badge&logo=Confluence&logoColor=white"/>
<img alt="VirtualBox" src="https://img.shields.io/badge/VirtualBox-183A61.svg?style=for-the-badge&logo=VirtualBox&logoColor=white"/>
<br/>
<br/>

![SeoYeons's GitHub stats](https://github-readme-stats.vercel.app/api?username=KimSeoYeon23&show_icons=true&theme=dark)
<br/>
<br/>
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=KimSeoYeon23&&theme=onedark&exclude_repo=github-readme-stats,anuraghazra.github.io)](https://github.com/KimSeoYeon23)
<br/>
</div>

## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
