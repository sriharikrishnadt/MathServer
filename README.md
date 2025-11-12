# Ex.05 Design a Website for Server Side Processing
## Date:12-11-2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
### MATH.HTML :
```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Power of Lamp in Incandescent Bulb</title>

  <style>
    body {
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        background: {{ bg_color }};
        transition: background 0.8s ease-in-out;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }


    .container {
      background: white;
      border-radius: 12px;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
      padding: 30px 40px;
      max-width: 500px;
      width: 90%;
    }

    h1 {
      text-align: center;
      color: #222;
      margin-bottom: 25px;
      font-size: 1.5rem;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    form {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }

    label {
      font-weight: 600;
      color: #333;
      margin-bottom: 5px;
      display: block;
    }

    input[type="text"] {
      width: 100%;
      padding: 8px 10px;
      font-size: 16px;
      border-radius: 6px;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }

    input[type="submit"] {
      background-color: #3b82f6;
      color: white;
      border: none;
      padding: 10px;
      font-size: 16px;
      border-radius: 6px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    input[type="submit"]:hover {
      background-color: #2563eb;
    }

    .result {
      background-color: #fff;
      padding: 8px;
      border-radius: 6px;
      border: 1px solid #ccc;
      text-align: center;
      font-weight: bold;
    }

    .unit {
      font-size: 0.9rem;
      color: #555;
      margin-left: 5px;
    }

    .error {
      color: red;
      text-align: center;
      font-weight: bold;
      margin-bottom: 10px;
    }
  </style>
</head>

<body>
  <div class="container">
    <h1>Power of Lamp in Incandescent Bulb</h1>

    {% if error %}
      <div class="error">{{ error }}</div>
    {% endif %}

    <form method="POST">
      {% csrf_token %}

      <div>
        <label for="intensity">Intensity</label>
        <input type="text" id="intensity" name="Intensity" value="{{ I }}" placeholder="Enter current in amperes" />
        <span class="unit">(A)</span>
      </div>

      <div>
        <label for="resistance">Resistance</label>
        <input type="text" id="resistance" name="Resistance" value="{{ R }}" placeholder="Enter resistance in ohms" />
        <span class="unit">(Ω)</span>
      </div>

      <div>
        <input type="submit" value="Calculate" />
      </div>

      <div>
        <label for="power">Power</label>
        <input type="text" id="power" name="Power" value="{{ Power }}" readonly class="result" />
        <span class="unit">W</span>
      </div>
    </form>
  </div>
</body>

</html>

```
### VIEWS.PY :
```
from django.shortcuts import render

def powerlamp(request):
    context = {
        'Power': '',
        'I': '',
        'R': '',
        'error': '',
        'bg_color': 'linear-gradient(90deg, rgb(99, 237, 118) 9%, rgb(193, 166, 202) 56%)'
    }

    # Internal variable (for backend usage)
    Power_value = None  

    if request.method == 'POST':
        print("✅ POST method used")
        
        # Correct field names — must match HTML
        I = request.POST.get('Intensity', '').strip()
        R = request.POST.get('Resistance', '').strip()

        print(f"📥 Input — Intensity: {I}, Resistance: {R}")

        try:
            if not I or not R:
                context['error'] = "⚠️ Please enter both Intensity and Resistance."
            else:
                # Convert to float
                I_val = float(I)
                R_val = float(R)

                # Calculate Power
                Power_value = round(I_val ** 2 * R_val, 2)

                # Save to context for HTML display
                context['Power'] = Power_value
                context['I'] = I_val
                context['R'] = R_val

                print(f"⚡ Power Calculated = {Power_value} W")

                # Optional: Background color logic based on Power
                if Power_value < 50:
                    context['bg_color'] = 'linear-gradient(90deg, #8EC5FC 0%, #E0C3FC 100%)'
                elif Power_value < 200:
                    context['bg_color'] = 'linear-gradient(90deg, #FAD961 0%, #F76B1C 100%)'
                else:
                    context['bg_color'] = 'linear-gradient(90deg, #ff9a9e 0%, #fad0c4 100%)'

        except ValueError:
            context['error'] = "❌ Invalid input! Please enter numeric values only."
            print("❌ Conversion error: Non-numeric input received.")

    if Power_value is not None:
        print(f"📊 (Internal) Power stored in backend variable: {Power_value} W")

    return render(request, 'mathapp/math.html', context)

```

### URLS.PY :
```
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.powerlamp,name="powerlamp"),]
```


## SERVER SIDE PROCESSING:
![alt text](<ex 5(1)-1.png>)

## HOMEPAGE:
![alt text](<ex 5-1.png>)

## RESULT:
The program for performing server side processing is completed successfully.
