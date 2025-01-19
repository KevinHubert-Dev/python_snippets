from flask import Flask, request, jsonify
from logic.reverse_string import reverse_string_logic
from logic.transpose_matrix import transpose_matrix_logic
from logic.extract_dict_list_property import extract_dict_list_property_logic
from logic.is_prime import primes_below
import time

app = Flask(__name__)

@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    data = request.json
    result = reverse_string_logic(data['string'])
    return jsonify(result)

@app.route('/transpose_matrix', methods=['POST'])
def transpose_matrix():
    data = request.json
    result = transpose_matrix_logic(data['matrix'])
    return jsonify(result)

@app.route('/extract_dict_list_property', methods=['POST'])
def extract_dict_list_property():
    data = request.json
    result = extract_dict_list_property_logic(data['dict_list'], data['property'])
    return jsonify(result)

@app.route('/count_primes_below', methods=['POST'])
def count_primes_below():
    data = request.json
    start_time = time.time()
    result = primes_below(data['number'])
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return jsonify({'result': result, 'time_ms': elapsed_time})


if __name__ == '__main__':
    app.run(debug=True)

