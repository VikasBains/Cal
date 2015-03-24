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
      end
    end

    flow width: 1.0, height: 0.8 do
      background rgb(139, 206, 23)
    end
  end
end
