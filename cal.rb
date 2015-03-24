require 'green_shoes'

Shoes.app(title: "My", width: 200, height: 240) do
  number_field = nil
  @number = 0

  flow width: 200, height: 240 do
    flow width: 0.7, height: 0.2 do
      background rgb(0, 157, 22)
      number_field = para @number, margin: 10
    end

    flow width: 0.3, height: 0.2 do
      button 'Clr', width: 1.0, height: 1.0 do
        @number = 0
        number_field.replace(@number)
      end
    end

    flow width: 1.0, height: 0.84 do
      background rgb(139, 206, 23)
      %w(7 8 9 + 4 5 6 - 1 2 3 / 0 . = *).each do |btn|
        button btn, width: 50, height: 50 do
        end
      end
    end
  end
end
