def organizar_eventos(*args):
    for i, evento in enumerate(args, 1):
        print(f"{i}. {evento}")

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")