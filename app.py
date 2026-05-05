from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 定義專案核心目標資料，方便前端渲染
    project_goals = [
        {
            "title": "GitHub Trending 30 大專案爬取",
            "desc": "自動抓取 GitHub 官方當週排名前 30 的開源專案，獲取專案名稱、描述及開發語言。",
            "icon": "🔍"
        },
        {
            "title": "自動化排程更新",
            "desc": "系統固定於每週一 00:00 執行自動爬蟲任務，無需人工介入，確保數據時效性。",
            "icon": "⏰"
        },
        {
            "title": "歷史排名紀錄儲存",
            "desc": "建立資料庫紀錄每週排名變動，讓使用者可以回溯查看過去特定時間點的技術趨勢。",
            "icon": "💾"
        },
        {
            "title": "連續上榜特別標記 (Streak)",
            "desc": "演算法自動比對歷史數據，針對連續 2 週以上上榜的優質專案給予熱力標籤。",
            "icon": "🔥"
        }
    ]
    
    context = {
        "title": "GitHub 趨勢追蹤與分析平台",
        "team_goal": "建立一個具備「自動化更新」與「熱度延續性分析」的開源專案觀察站。",
        "goals": project_goals
    }
    
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)