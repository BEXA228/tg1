def Detection():
	import pathlib
	import numpy as np
	import tensorflow as tf

	from tensorflow.keras import layers
	from tensorflow.keras.models import Sequential

	dataset_dir = pathlib.Path("archive2")
	batch_size = 32
	img_width = 180
	img_height = 180

	train_ds = tf.keras.utils.image_dataset_from_directory(
	dataset_dir,
	validation_split=0.2,
	subset="training",
	seed=123,
	image_size=(img_height, img_width),
	batch_size=batch_size)

	val_ds = tf.keras.utils.image_dataset_from_directory(
	dataset_dir,
	validation_split=0.2,
	subset="validation",
	seed=123,
	image_size=(img_height, img_width),
	batch_size=batch_size)

	class_names = train_ds.class_names
	print(f"Class names: {class_names}")

	# create model
	num_classes = len(class_names)
	model = Sequential([
	# т.к. у нас версия TF 2.6 локально
	layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),

	# дальше везде одинаково
	layers.Conv2D(16, 3, padding='same', activation='relu'),
	layers.MaxPooling2D(),

	layers.Conv2D(32, 3, padding='same', activation='relu'),
	layers.MaxPooling2D(),

	layers.Conv2D(64, 3, padding='same', activation='relu'),
	layers.MaxPooling2D(),

	layers.Flatten(),
	layers.Dense(128, activation='relu'),
	layers.Dense(num_classes)
	])

	# compile the model
	model.compile(
	optimizer='adam',
	loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
	metrics=['accuracy'])

	#load model
	model.load_weights("my_model.h5")

	#evaluate the model
	loss, acc = model.evaluate(train_ds, verbose=2)
	print("Restored model, accuracy: {:5.2f}%".format(100 * acc))

	# load image
	img = tf.keras.utils.load_img("photo.jpg", target_size=(img_height, img_width))
	img_array = tf.keras.utils.img_to_array(img)
	img_array = tf.expand_dims(img_array, 0)

	# make predictions
	predictions = model.predict(img_array)
	score = tf.nn.softmax(predictions[0])

	#print inferenc result
	Result = "tf_gpu утверждает, что на изображении скорее всего {} вероятность - {:.2f}%".format(
	class_names[np.argmax(score)],
	100 * np.max(score))
	print(Result)
	return Result

# Detection()

