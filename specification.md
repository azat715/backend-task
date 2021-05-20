# Тестовое задание
Есть абстрактная компания, которая доставляет воду. Они подумали, что в 2020 принимать заявки по телефону это совсем не прогрессивно и решили, что дадут своим любимым клиентам возможность заказа онлайн.

**Задача:** разработать API и интерфейс для приема заказов. В качестве интерфейса может быть телеграм-бот (предпочтительно), plain-html форма или любое, что придет в голову. Главное — заявки должны фиксироваться в базе данных.

## Процесс заказа

1. Ввод ФИО
2. Ввод e-mail
3. Ввод телефона
4. Ввод адреса доставки
5. Ввод количества желаемых бутылей воды
6. Ввод даты доставки
7. Выбор интервала времени доставки (особенность — по будням доступны интервалы доставки: 10-11:00, 12-13:00 и 15-16:00, а по выходным только 12-13:00 и 15-16:00).
8. Отправка заказа

## Пример метода для заведения и получения заявок на воду

### POST domain.com/order

    // Request
    {
    	user: {
        name: "Иванов Иван Иванович",
        phone: "79171112233",
    		email: "ivan@mail.ru"
      },
      address: "Самара, Мичурина 21, офис 501",
      qty: 1,
    	date: "2020-02-25",
      time: "10:00 - 14:00"
    }
    
    // Response
    {
    	status: "success",
    	order_id: 141
    }

### GET domain.com/order/list

    // Response
    {
    	data: [...] // массив заказов, таких же как запросы, только с доп. полями "created_at" и "id"
    }

## Задача минимум
- Сделать API для фиксации заказов и возможности их получения (Create и Read из CRUD)

## Задача максимум
- Реализовать интерфейс в виде телеграм-бота, веб-формы или в любом другом виде
- Реализовать логику разных интервалов в зависимости от дня недели
- Добавить валидации на ввод данных пользователем

## Будет бонусом
- Единый код-стайл и использование [линтера](https://eslint.org/)
- Ведение коммитов git-а по ходу выполнения
- Покрытие тестами
- Интерфейс для просмотра всех поступивших заказов
- Возможность отмены заказа

# Как делать тестовое?
Как тебе угодно! Мы постарались сделать тестовое задание интересным и не совсем простым, чтобы был какой-то challenge. Но в то же время мы не хотим, чтобы ты тратил(а) на него много времени. Для нас главное — объективно оценить навыки кандидатов и дать полезную обратную связь тем, кто не пройдет в этом наборе.

> Самый удобный формат — сделать форк нашего репозитория, и по завершению прислать pull request с выполненным заданием. Пример того, как может выглядеть форк после пулл реквеста - папка "Иванов Иван Иванович".

**НО!** это только рекомендация, если тебе удобно делать иначе — без проблем. Для нас важно понять способность кандидата решать подобные задачи. Результат тестового можно также отправить на artem@anmedio.ru.

**Критерии этого задания**, по которым будет проводится оценка: архитектура БД, структура кода, паттерны проектирования, целостность хранения данных и качество кода. Более детальную оценку по заданию будем отправлять кандидатам после завершения.

> Если остались вопросы — почта artem@anmedio.ru или телеграм @artyom_ivanov

# Материалы
Есть макет из тестового задания для фронтенда, где можно "подглядеть" то, как это выглядело бы с полноценным интерфейсом — макет доступен [по ссылке в режиме просмотра](https://www.figma.com/file/iqKdXp063fMoEFD7oZHxVS/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5-frontend?node-id=1%3A66) или файлом тут же в репозитории (это фигма).