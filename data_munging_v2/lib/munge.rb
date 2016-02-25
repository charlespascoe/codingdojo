class Weather
  def open filename
    File.readlines filename
  end

  def parseline line
    line.split(/\s+/).reject(&:empty?).map(&:to_f)
  end

  def parselines lines
    lines.last(lines.length-2).map{|x| parseline x}
  end

  def tempspread data
    data[1] - data[2]
  end

  def mintempspread lines
    lines.min_by{|x| tempspread x}[0]
  end

  def answer filename
    mintempspread parselines open filename
  end
end
