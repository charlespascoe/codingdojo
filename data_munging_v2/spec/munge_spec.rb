require 'munge'

describe Weather do
  describe '#parseline' do
    it 'returns an array of data' do
      expect(subject.parseline(' 1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5')).to eq [1, 88, 59, 74, 53.8, 0.00, 0, 280, 9.6, 270, 17, 1.6, 93, 23, 1004.5]
      expect(subject.parseline(' 17  81    57    69          51.7       0.00 T       260  9.1 270  29* 5.2  90 34 1012.5')).to eq [17, 81, 57, 69, 51.7, 0.00, 0, 260, 9.1, 270, 29, 5.2, 90, 34, 1012.5]
      expect(subject.parseline('   9  86    32*   59       6  61.5       0.00         240  7.6 220  12  6.0  78 46 1018.6')).to eq [9, 86, 32, 59, 6, 61.5, 0.00, 240, 7.6, 220, 12, 6.0, 78, 46, 1018.6]
    end
  end

  describe '#tempspread' do
    it 'returns correct temperature spread' do
      expect(subject.tempspread([1, 88, 59, 74, 53.8, 0.00, 0, 280, 9.6, 270, 17, 1.6, 93, 23, 1004.5])).to eq 29
      expect(subject.tempspread([17, 81, 57, 69, 51.7, 0.00, 0, 260, 9.1, 270, 29, 5.2, 90, 34, 1012.5])).to eq 24
      expect(subject.tempspread([9, 86, 32, 59, 6, 61.5, 0.00, 240, 7.6, 220, 12, 6.0, 78, 46, 1018.6])).to eq 54
    end
  end

  describe '#parselines' do
    it 'returns correct rows for test.txt' do
      expect(subject.parselines(File.readlines('test.txt'))).to eq [[1,3,0],[2,42.1,-1],[3,23,2]]
    end
  end

  describe '#mintempspread' do
    it 'returns the day with the minimum temp spread' do
      expect(subject.mintempspread([[1,3,0],[2,42.1,-1],[3,23,2]])).to eq 1
    end
  end

  describe '#answer' do
    it 'returns the answer' do
      expect(subject.answer('test.txt')).to eq 1
      expect(subject.answer('weather.txt')).to eq 14
    end
  end
end
