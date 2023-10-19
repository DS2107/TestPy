from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    #Запоминает соответствующие аргументы конечной точки и представления
    args = request.args
    
   # Возвращаю страницу , на которой ищу аргументы name, message и подставляю туда значения
    return render_template(
        'index.html', 
        name= args.get('name') if args.get('name') else 'В поисковой строке добавьте', 
        message=args.get('message') if args.get('message') else '/?name=Rekruto&message=Давай%20дружить!'
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0')


