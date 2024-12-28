from flask import Flask, request, jsonify
import csv
import io

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_csv_to_pgn():
    """
    Accepts a CSV file containing chess moves and returns a PGN-formatted response.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty file"}), 400

    try:
        # Parse the CSV file
        csv_file = io.TextIOWrapper(file.stream, encoding='utf-8')
        reader = csv.reader(csv_file)
        moves = []
        for row in reader:
            if len(row) >= 2:  # Expect moves in two columns (White, Black)
                moves.append(row[:2])  # Take the first two columns (White, Black)
            elif len(row) == 1:  # If only one move (White), append empty Black
                moves.append([row[0], ""])
        
        # Convert moves to PGN format
        pgn = convert_to_pgn(moves)
        return jsonify({"pgn": pgn}), 200
    
    except Exception as e:
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500

def convert_to_pgn(moves):
    """
    Converts a list of chess moves to PGN format.
    """
    pgn = []
    for i, move_pair in enumerate(moves):
        move_number = i + 1
        white_move = move_pair[0]
        black_move = move_pair[1] if len(move_pair) > 1 else ''
        pgn.append(f"{move_number}. {white_move} {black_move}")
    return "\n".join(pgn)

if __name__ == '__main__':
    app.run(debug=True)
