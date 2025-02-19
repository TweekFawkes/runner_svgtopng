import argparse
import os

try:
    import cairosvg
except ImportError:
    print("Please install cairosvg first: pip install cairosvg")
    exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--svg_file', required=True, help='Input image file name (SVG) from inputs directory')
    args = parser.parse_args()
    
    # Validate file extension
    if not args.svg_file.lower().endswith('.svg'):
        print(f"Error: Input file must be an SVG file")
        return 1
    
    # Construct full input path
    input_path = os.path.join('inputs', args.svg_file)
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist")
        return 1

    try:
        # Create outputs directory if it doesn't exist
        os.makedirs('outputs', exist_ok=True)
        
        # Create output filename in outputs directory
        base_name = os.path.splitext(args.svg_file)[0]
        output_file = os.path.join('outputs', f"{base_name}.png")
        
        # Check if output file already exists
        if os.path.exists(output_file):
            print(f"Warning: Output file '{output_file}' already exists and will be overwritten")
        
        # Check if input file is readable
        if not os.access(input_path, os.R_OK):
            print(f"Error: Input file '{input_path}' is not readable")
            return 1
            
        # Convert SVG to PNG
        cairosvg.svg2png(url=input_path, write_to=output_file)
        print(f"Successfully converted {input_path} to {output_file}")
        return 0
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return 1

if __name__ == "__main__":
    exit(main())