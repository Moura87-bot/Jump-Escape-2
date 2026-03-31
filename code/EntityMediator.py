class EntityMediator:

    @staticmethod
    def verify_collision(entity_list, level):

        for ent in entity_list:

            # 💥 TIRO DO PLAYER
            if ent.name == 'Player1Bullet' or ent.name == 'Player2Bullet':
                for target in entity_list:
                    if target.name.startswith('Enemy'):
                        if ent.rect.colliderect(target.rect):
                            ent.health = 0
                            target.health -= 1

                            if target.health <= 0:
                                level.score += 100
                                print("INIMIGO MORTO +100")

            # 💥 TIRO DO INIMIGO
            if ent.name == 'Enemy1Bullet':
                for target in entity_list:
                    if target.name.startswith('Player'):
                        if ent.rect.colliderect(target.rect):
                            ent.health = 0
                            target.health -= 1
                            print("PLAYER ATINGIDO")

    @staticmethod
    def verify_health(entity_list):
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]