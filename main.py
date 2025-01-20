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
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 20px auto;
            background-color: #fff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #0056b3;
            font-size: 2.5em;
        }
        .college-list {
            list-style: none;
            padding: 0;
        }
        .college-item {
             display: flex;
            align-items: center;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;

        }
          .college-item:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        .college-item img {
            width: 100px;
            height: 100px;
            border-radius: 8px;
            margin-right: 20px;
            object-fit: cover;
             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .college-item h2 {
            font-size: 1.5em;
             margin-bottom: 5px;
            color: #0056b3;
        }
         .college-item p {
           font-size: 0.9em;
           margin-bottom: 10px;
            line-height: 1.4;
        }

        .college-item a {
           color: #007bff;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
             margin-top: 10px;
            display: inline-block;
        }
         .college-item a:hover {
            text-decoration: underline;
            color: #0056b3;
        }

    </style>
</head>
<body>
    <div class="container">
        <h1>Колледжи Владимира</h1>
        <p>Добро пожаловать на страницу с информацией о колледжах города Владимира! Здесь вы найдете список учебных заведений с кратким описанием и ссылками на их официальные сайты.</p>
        <ul class="college-list">
             <li class="college-item">
                <img src="" alt="Владимирский техникум экономики и информатики" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                <div>
                     <h2>Владимирский техникум экономики и информатики</h2>
                    <p>Современное учебное заведение, предлагающее широкий спектр программ в области экономики и информационных технологий.</p>
                    <a href="https://www.vladimirteh.ru/" target="_blank">Официальный сайт</a>
                </div>
            </li>
            <li class="college-item">
                <img src="" alt="Владимирский областной медицинский колледж" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                 <div>
                    <h2>Владимирский областной медицинский колледж</h2>
                    <p>Один из ведущих медицинских колледжей региона, готовящий квалифицированных медицинских специалистов.</p>
                    <a href="https://vladimir.medcollege.ru/" target="_blank">Официальный сайт</a>
                   </div>
            </li>
             <li class="college-item">
               <img src="" alt="Владимирский колледж технологий и машиностроения" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                <div>
                    <h2>Владимирский колледж технологий и машиностроения</h2>
                    <p>Колледж с многолетней историей, специализирующийся на подготовке специалистов в сфере машиностроения и технологий.</p>
                    <a href="https://www.vkmt.ru/" target="_blank">Официальный сайт</a>
                 </div>
            </li>
              <li class="college-item">
                 <img src="" alt="Владимирский губернский педагогический колледж" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                <div>
                    <h2>Владимирский губернский педагогический колледж</h2>
                    <p>Готовит высококвалифицированных педагогов для работы в образовательных учреждениях.</p>
                    <a href="https://www.vgpk.ru/" target="_blank">Официальный сайт</a>
                    </div>
            </li>
               <li class="college-item">
                 <img src="" alt="Владимирский гидрометеорологический техникум" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                 <div>
                    <h2>Владимирский гидрометеорологический техникум</h2>
                    <p>Специализируется на подготовке специалистов в области гидрометеорологии и смежных дисциплин.</p>
                    <a href="https://www.vgzt.ru/" target="_blank">Официальный сайт</a>
                  </div>
            </li>
            <li class="college-item">
                <img src="" alt="Владимирский кооперативный техникум" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                  <div>
                    <h2>Владимирский кооперативный техникум</h2>
                     <p>Учебное заведение, специализирующееся на подготовке специалистов в области потребительской кооперации.</p>
                    <a href="https://www.vkt.avo.ru/" target="_blank">Официальный сайт</a>
                   </div>
            </li>
             <li class="college-item">
                 <img src="" alt="Владимирское музыкальное училище им. А.П. Бородина" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                <div>
                    <h2>Владимирское музыкальное училище им. А.П. Бородина</h2>
                     <p>Одно из старейших музыкальных учебных заведений России, предлагающее обучение по различным музыкальным направлениям.</p>
                    <a href="https://vlmu.ru/" target="_blank">Официальный сайт</a>
                  </div>
            </li>
             <li class="college-item">
                 <img src="" alt="Владимирский авиамеханический колледж" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                  <div>
                    <h2>Владимирский авиамеханический колледж</h2>
                    <p>Специализируется на подготовке специалистов для авиационной промышленности.</p>
                    <a href="http://www.vlatp.ru/" target="_blank">Официальный сайт</a>
                   </div>
            </li>
            <li class="college-item">
                 <img src="" alt="Владимирский муниципальный колледж" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                   <div>
                     <h2>Владимирский муниципальный колледж</h2>
                    <p>Многопрофильный колледж, предоставляющий образование в различных областях.</p>
                    <a href="https://www.vladmkk.ru/" target="_blank">Официальный сайт</a>
                   </div>
            </li>
            <li class="college-item">
                <img src="" alt="Владимирский промышленно-коммерческий техникум" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                 <div>
                     <h2>Владимирский промышленно-коммерческий техникум</h2>
                      <p>Обучает специалистов в сфере промышленности и торговли.</p>
                    <a href="https://www.vlpt.ru/" target="_blank">Официальный сайт</a>
                   </div>
            </li>
              <li class="college-item">
                <img src="" alt="Владимирский колледж градостроительства и дизайна" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                 <div>
                    <h2>Владимирский колледж градостроительства и дизайна</h2>
                    <p>Обучает специалистов в сфере градостроительства, архитектуры и дизайна.</p>
                    <a href="http://www.vgkh.ru/" target="_blank">Официальный сайт</a>
                 </div>
            </li>
            <li class="college-item">
                 <img src="" alt="Владимирский колледж инновационных технологий" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
               <div>
                    <h2>Владимирский колледж инновационных технологий</h2>
                    <p>Современный колледж, предлагающий образовательные программы в области инновационных технологий.</p>
                    <a href="https://www.vkik.avo.ru/" target="_blank">Официальный сайт</a>
                </div>
            </li>
            <li class="college-item">
                 <img src="" alt="Колледж Владимирского государственного университета" onerror="this.src='https://via.placeholder.com/100x100?text=No+Image';">
                 <div>
                    <h2>Колледж Владимирского государственного университета</h2>
                    <p>Подразделение ВлГУ, предлагающее программы среднего профессионального образования.</p>
                     <a href="https://www.vtsu.ru/struktura/fakultety_instituty/fakultet_tekhnicheskikh_sistem_obsluzhivaniya/kolledzh/" target="_blank">Официальный сайт</a>
                </div>
            </li>
        </ul>
    </div>
</body>
</html>
    """
    return html_content