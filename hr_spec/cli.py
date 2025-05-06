import argparse
from hr_spec import stellar

def main():
    parser = argparse.ArgumentParser(description='HR-Spec Stellar Tools')
    
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Predict_evolution parser
    predict = subparsers.add_parser('predict')
    predict.add_argument('--mass', type=float, required=True)
    predict.add_argument('--metallicity', type=float, required=True)
    predict.add_argument('--age', type=float, required=True)
    
    # Classify star parser
    classify = subparsers.add_parser('classify')
    classify.add_argument('--temperature', type=float, required=True)
    classify.add_argument('--luminosity', type=float, required=True)
    
    args = parser.parse_args()
    
    if args.command == 'predict':
        result = stellar.predict_evolution(args.mass, args.metallicity, args.age)
        print(result)
    elif args.command == 'classify':
        result = stellar.classify(args.temperature, args.luminosity)
        print(result)

if __name__ == '__main__':
    main()