import jsonlines
import argparse
import requests

def generate_prompt(instruction):
    """
    Generates a prompt for the model based on the instruction.
    """
    return f'''Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:'''

def make_request(prompt, base_url="http://localhost:1234/v1/completions"):
    """
    Makes a request to the server to generate a completion for the given prompt.
    """
    data = {"prompt": prompt}
    response = requests.post(base_url, json=data)
    if response.status_code == 200:
        return response.json().get('text', '')
    else:
        print(f"Error: Server responded with status code {response.status_code}")
        return None

def process_file(input_data_path, output_data_path, base_model):
    """
    Processes the input file, generates responses, and writes them to the output file.
    """
    with jsonlines.open(input_data_path, mode='r') as input_file, \
            jsonlines.open(output_data_path, mode='w') as output_file:

        for line in input_file:
            idx = line["idx"]
            instruction = line["Instruction"]
            prompt = generate_prompt(instruction)
            response = make_request(prompt, base_model)

            output_file.write({
                "id": idx,
                "instruction": instruction,
                "response": response
            })

def main():
    parser = argparse.ArgumentParser(description='WizardCoder Inference Script')
    parser.add_argument('--input_data_path', required=True, help='Path to input data.jsonl file')
    parser.add_argument('--output_data_path', required=True, help='Path to output result.jsonl file')
    args = parser.parse_args()

    process_file(args.input_data_path, args.output_data_path, args.base_model)

if __name__ == "__main__":
    main()