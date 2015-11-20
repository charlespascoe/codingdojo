require 'string_calculator'

describe Calculator do
  describe '#add' do
    it 'returns 0 for empty string' do
      expect(subject.add '').to eq 0
    end
    it 'returns a number when there is one number' do
      expect(subject.add '4').to eq 4
      expect(subject.add '-188').to eq -188
      expect(subject.add '678').to eq 678
      expect(subject.add '0').to eq 0
      expect(subject.add '1.64').to eq 1.64
      expect(subject.add '-12.768').to eq -12.768
    end
    it 'returns the sum of two numbers' do
      expect(subject.add '0,0').to eq 0
      expect(subject.add '0,1').to eq 1
      expect(subject.add '7,14').to eq 21
      expect(subject.add '-15,0').to eq -15
      expect(subject.add '10.56,-5.32').to eq 5.24
      expect(subject.add '0,65.356').to eq 65.356
      expect(subject.add '1,-4.7').to eq -3.7
    end
    it 'returns the sum of more than two numbers' do
      expect(subject.add '0,1,2,3').to eq 6
      expect(subject.add '6,5,4,3,2,100').to eq 120
    end
    it 'allows newline delimiters' do
      expect(subject.add '0\n3').to eq 3
      expect(subject.add '100').to eq 100
      expect(subject.add '1,0\n3').to eq 4
      expect(subject.add '1\n1.1').to eq 2.1
    end
    it 'allows adding custom delimeters' do
      expect(subject.add '//;\n3;7;4').to eq 14
      expect(subject.add '//[\n3[7[4').to eq 14
      expect(subject.add '//$\n3$7$4').to eq 14
      expect(subject.add '//\\\n3\\7\\4').to eq 14
      expect(subject.add '//hello\n3hello12hello0').to eq 15
    end
  end
end
