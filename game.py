from firebase_admin import firestore

class Game:
    @staticmethod
    def start(form):
        db = firestore.client()
        game = db.collection('games').document()
        game.set({
            'player1': form['player1'],
            'player2': form['player2'],
            'status': 'in_progress',
            'moves': []
        })
        return game.id

    @staticmethod
    def join(game_id, player_id):
        db = firestore.client()
        game = db.collection('games').document(game_id)
        game.update({
            'player2': player_id
        })
        return game.id

    @staticmethod
    def make_move(game_id, move):
        db = firestore.client()
        game = db.collection('games').document(game_id)
        game.update({
            'moves': firestore.ArrayUnion([move])
        })
        return game.id

    @staticmethod
    def check_status(game_id):
        db = firestore.client()
        game = db.collection('games').document(game_id)
        return game.get().to_dict()['status']
