from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Колледжи Владимира</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f7f6;
            color: #333;
            line-height: 1.6;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 20px auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #0056b3;
            font-size: 2.8em;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.05);
        }
        .college-grid {
           display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
        }
        .college-card {
             background-color: #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
          .college-card:hover {
            transform: translateY(-5px);
        }
         .college-card img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-bottom: 20px;
            object-fit: cover;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
              transition: transform 0.3s ease;

        }
          .college-card img:hover {
           transform: scale(1.1);
        }
        .college-card h2 {
            font-size: 1.8em;
            margin-bottom: 10px;
            color: #0056b3;
             text-align: center;
        }
         .college-card p {
            margin-bottom: 20px;
            text-align: justify;
        }
        .college-card a {
            display: inline-block;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            padding: 12px 20px;
            border-radius: 5px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .college-card a:hover {
            background-color: #0056b3;
        }
         footer {
            text-align: center;
             padding: 20px 0;
            background-color: #343a40;
            color: #fff;
             margin-top: 20px;
         }

         @media (max-width: 768px) {
            .container {
                width: 95%;
                padding: 20px;
            }
             .college-grid {
               grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            }
             .college-card img{
               width: 120px;
                height: 120px;
             }
             .college-card h2{
                font-size: 1.5em;
            }
             .college-card p {
                 text-align: left;
             }
            h1{
                font-size: 2.2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Колледжи Владимира</h1>
        <p style="text-align: center; font-size:1.1em; color:#666; margin-bottom: 30px;">Добро пожаловать на страницу с информацией о колледжах города Владимира! Здесь вы найдете список учебных заведений с кратким описанием и ссылками на их официальные сайты.</p>
       <div class="college-grid">
           <div class="college-card">
                <img src="" alt="Владимирский техникум экономики и информатики" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский техникум экономики и информатики</h2>
                <p>Современное учебное заведение, предлагающее широкий спектр программ в области экономики и информационных технологий.
                </p>
                <a href="https://www.vladimirteh.ru/" target="_blank">Официальный сайт</a>
            </div>
             <div class="college-card">
                <img src="" alt="Владимирский областной медицинский колледж" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский областной медицинский колледж</h2>
                <p>Один из ведущих медицинских колледжей региона, готовящий квалифицированных медицинских специалистов.
                </p>
                <a href="https://vladimir.medcollege.ru/" target="_blank">Официальный сайт</a>
            </div>
            <div class="college-card">
                <img src="" alt="Владимирский колледж технологий и машиностроения" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский колледж технологий и машиностроения</h2>
               <p>Колледж с многолетней историей, специализирующийся на подготовке специалистов в сфере машиностроения и технологий.
                </p>
                <a href="https://www.vkmt.ru/" target="_blank">Официальный сайт</a>
           </div>
          <div class="college-card">
              <img src="" alt="Владимирский губернский педагогический колледж" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский губернский педагогический колледж</h2>
                <p>Готовит высококвалифицированных педагогов для работы в образовательных учреждениях.
                </p>
                 <a href="https://www.vgpk.ru/" target="_blank">Официальный сайт</a>
           </div>
            <div class="college-card">
               <img src="" alt="Владимирский гидрометеорологический техникум" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский гидрометеорологический техникум</h2>
                <p>Специализируется на подготовке специалистов в области гидрометеорологии и смежных дисциплин.
                </p>
                <a href="https://www.vgzt.ru/" target="_blank">Официальный сайт</a>
            </div>
             <div class="college-card">
               <img src="" alt="Владимирский кооперативный техникум" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский кооперативный техникум</h2>
                <p>Учебное заведение, специализирующееся на подготовке специалистов в области потребительской кооперации.
                </p>
                <a href="https://www.vkt.avo.ru/" target="_blank">Официальный сайт</a>
            </div>
            <div class="college-card">
               <img src="" alt="Владимирское музыкальное училище им. А.П. Бородина" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирское музыкальное училище им. А.П. Бородина</h2>
                <p>Одно из старейших музыкальных учебных заведений России, предлагающее обучение по различным музыкальным направлениям.
                </p>
                 <a href="https://vlmu.ru/" target="_blank">Официальный сайт</a>
            </div>
              <div class="college-card">
                 <img src="" alt="Владимирский авиамеханический колледж" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский авиамеханический колледж</h2>
                <p>Специализируется на подготовке специалистов для авиационной промышленности.
                </p>
                <a href="http://www.vlatp.ru/" target="_blank">Официальный сайт</a>
            </div>
             <div class="college-card">
                 <img src="" alt="Владимирский муниципальный колледж" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский муниципальный колледж</h2>
                 <p>Многопрофильный колледж, предоставляющий образование в различных областях.
                </p>
                <a href="https://www.vladmkk.ru/" target="_blank">Официальный сайт</a>
             </div>
             <div class="college-card">
               <img src="" alt="Владимирский промышленно-коммерческий техникум" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский промышленно-коммерческий техникум</h2>
                <p>Обучает специалистов в сфере промышленности и торговли.
                 </p>
                 <a href="https://www.vlpt.ru/" target="_blank">Официальный сайт</a>
            </div>
           <div class="college-card">
                <img src="" alt="Владимирский колледж градостроительства и дизайна" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский колледж градостроительства и дизайна</h2>
                <p>Обучает специалистов в сфере градостроительства, архитектуры и дизайна.
               </p>
                <a href="https://www.vgkh.ru/" target="_blank">Официальный сайт</a>
            </div>
            <div class="college-card">
                 <img src="" alt="Владимирский колледж инновационных технологий" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Владимирский колледж инновационных технологий</h2>
                <p>Современный колледж, предлагающий образовательные программы в области инновационных технологий.
                 </p>
                 <a href="https://www.vkik.avo.ru/" target="_blank">Официальный сайт</a>
            </div>
              <div class="college-card">
               <img src="" alt="Колледж Владимирского государственного университета" onerror="this.src='https://via.placeholder.com/150x150?text=No+Image';">
                <h2>Колледж Владимирского государственного университета</h2>
                <p>Подразделение ВлГУ, предлагающее программы среднего профессионального образования.
                </p>
                 <a href="https://www.vtsu.ru/struktura/fakultety_instituty/fakultet_tekhnicheskikh_sistem_obsluzhivaniya/kolledzh/" target="_blank">Официальный сайт</a>
            </div>
        </div>
    </div>
       <footer>
            <p>&copy; 2024 All rights reserved.</p>
        </footer>
</body>
</html>
    """
    return html_content