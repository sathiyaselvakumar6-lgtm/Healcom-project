import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healcom.settings')
django.setup()

from core.models import EducationalResource

resources = [
    {
        'title': 'The Orthopedic Recovery Blueprint',
        'description': 'A comprehensive guide to bone and joint healing, including nutrition and safe mobility exercises.',
        'price': 499.00,
        'content': '''
            <h2>Welcome to your Recovery Blueprint</h2>
            <p>Recovering from orthopedic surgery requires a balanced approach. This guide covers the three pillars of success:</p>
            <ul>
                <li><strong>Nutrition:</strong> High protein and calcium intake are critical for bone density and tissue repair.</li>
                <li><strong>Mobility:</strong> Controlled, low-impact movements prevent stiffness (ankylosis) and blood clots.</li>
                <li><strong>Pain Management:</strong> Understanding the difference between "good pain" (rehab) and "bad pain" (injury).</li>
            </ul>
            <h2>Day 1-7 Protocol</h2>
            <p>Focus on RICE (Rest, Ice, Compression, Elevation). Do not overexert. Your primary goal is inflammation reduction.</p>
        '''
    },
    {
        'title': 'Cardiac Wellness & Strength',
        'description': 'Understanding heart-healthy habits and stress management after surgery.',
        'price': 799.00,
        'content': '''
            <h2>Your Heart, Re-imagined</h2>
            <p>Post-cardiac surgery is a new chapter. Let's make it your healthiest one yet.</p>
            <h3>Daily Habits</h3>
            <p>Monitoring your blood pressure and heart rate twice daily (morning and evening) is mandatory. Record these in your logs.</p>
            <h3>Dietary Adjustments</h3>
            <p>The DASH diet is highly recommended. Reduce sodium to under 1,500mg per day to prevent fluid retention.</p>
        '''
    },
    {
        'title': 'Mindful Healing: Mental Health Guide',
        'description': 'Techniques to manage anxiety and stay motivated during long recovery periods.',
        'price': 299.00,
        'content': '''
            <h2>Healing is 50% Mental</h2>
            <p>It is normal to feel frustrated or depressed during slow recovery. This module teaches you cognitive reframing.</p>
            <h3>Meditation for Pain</h3>
            <p>Research shows that 10 minutes of daily mindfulness can reduce perceived pain levels by up to 30%.</p>
        '''
    }
]

for r in resources:
    obj, created = EducationalResource.objects.get_or_create(
        title=r['title'],
        defaults={
            'description': r['description'],
            'price': r['price'],
            'content': r['content'],
            'is_active': True
        }
    )
    if created:
        print(f"Created: {r['title']}")
    else:
        print(f"Exists: {r['title']}")
