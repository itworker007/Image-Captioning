import os

img_rows, img_cols = 224, 224
channel = 3
batch_size = 64
epochs = 10000
patience = 50
num_train_samples = 210000 * 5 / 10
num_valid_samples = 30000 * 5 / 10
embedding_size = 300
vocab_size = 17627
max_token_length = 40
num_image_features = 2048

rnn_type = 'lstm'
bidirectional_rnn = False
hidden_size = 256

train_folder = 'data/ai_challenger_caption_train_20170902'
valid_folder = 'data/ai_challenger_caption_validation_20170910'
test_a_folder = 'data/ai_challenger_caption_test_a_20180103'
test_b_folder = 'data/ai_challenger_caption_test_b_20180103'
train_image_folder = os.path.join(train_folder, 'caption_train_images_20170902')
valid_image_folder = os.path.join(valid_folder, 'caption_validation_images_20170910')
test_a_image_folder = os.path.join(test_a_folder, 'caption_test_a_images_20180103')
test_b_image_folder = os.path.join(test_b_folder, 'caption_test_b_images_20180103')
train_annotations_filename = 'caption_train_annotations_20170902.json'
valid_annotations_filename = 'caption_validation_annotations_20170910.json'

start_word = '<start>'
stop_word = '<end>'
unknown_word = '<UNK>'
