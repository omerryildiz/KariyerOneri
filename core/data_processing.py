import spacy
import pre_processing

input_file_path="C:/Users/omeryildiz/Desktop/KariyerOneri/text_file/10089434.txt"
output_file_path ="output.txt"

text = pre_processing.load_file(input_file_path)

tokens = pre_processing.tokenize_text(text)

preprocessed_text = pre_processing.preprocess_text(input_file_path)

pre_processing.save_preprocessed_text(preprocessed_text,output_file_path)

