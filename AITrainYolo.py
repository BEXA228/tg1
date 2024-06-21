def Detection():

    from ultralytics import YOLO
    from PIL import Image

    # Обученная модель
    model = YOLO('best.pt')

    # Изображение для проверки
    img = Image.open('photo.jpg')

    # Предсказание
    results = model(img)

    # Сохраняем результат
    results[0].plot()
    output_path = 'output.jpg'
    results[0].save(output_path)

Detection()

