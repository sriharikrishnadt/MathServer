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
