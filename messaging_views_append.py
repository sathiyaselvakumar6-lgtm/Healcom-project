

# ─── MESSAGING API ────────────────────────────────────────
@login_required
def message_detail_api(request, message_id):
    message = get_object_or_404(DoctorMessage, id=message_id)
    # Ensure user has access
    if request.user != message.patient and request.user != message.doctor:
        return HttpResponseForbidden("Access Denied")
    
    return render(request, 'patient/message_detail_partial.html', {'message': message})


@login_required
@csrf_exempt
def mark_message_read_api(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(DoctorMessage, id=message_id)
        if request.user == message.patient:
            message.is_read = True
            message.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)


@login_required
@csrf_exempt
def mark_all_messages_read_api(request):
    if request.method == 'POST':
        DoctorMessage.objects.filter(patient=request.user, is_read=False).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)


@login_required
def compose_message_api(request):
    # For patients sending to their assigned doctor
    patient_profile = getattr(request.user, 'patient_profile', None)
    if not patient_profile or not patient_profile.assigned_doctor:
        if request.method == 'GET':
             return HttpResponse("Error: No assigned doctor found. Please contact support.")
        return JsonResponse({'status': 'error', 'message': 'No assigned doctor'}, status=400)

    if request.method == 'POST':
        topic   = request.POST.get('topic', 'general')
        content = request.POST.get('message', '').strip()
        
        if content:
            DoctorMessage.objects.create(
                doctor=patient_profile.assigned_doctor,
                patient=request.user,
                custom_message=f"[{topic.upper()}] {content}",
                is_from_patient=True
            )
            messages.success(request, "Message sent to your doctor.")
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Empty message'}, status=400)

    # GET request: return form
    context = {
        'assigned_doctor': patient_profile.assigned_doctor
    }
    return render(request, 'patient/compose_message_partial.html', context)
