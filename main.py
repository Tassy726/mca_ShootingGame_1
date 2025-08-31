def on_on_overlap(sprite, otherSprite):
    info.change_score_by(10)
    sprites.destroy(otherSprite, effects.fire, 100)
    sprites.destroy(sprite)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    sprites.destroy(otherSprite2)
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 1 2 . . . . . . 
                    . . . . . . . 2 1 2 . . . . . . 
                    . . . . . . . 2 1 2 . . . . . . 
                    . . . . . . . 3 1 3 . . . . . . 
                    . . . . . . 2 3 1 3 2 . . . . . 
                    . . . . . . 2 1 1 1 2 . . . . . 
                    . . . . . . 2 1 1 1 3 . . . . . 
                    . . . . . . 3 1 1 1 3 . . . . . 
                    . . . . . . 3 1 1 1 3 . . . . . 
                    . . . . . . 3 1 1 1 3 . . . . . 
                    . . . . . . 2 3 1 3 2 . . . . . 
                    . . . . . . . 2 2 2 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        0,
        -100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

projectile2: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c b . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . c 2 . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . e 2 . . . . . . . 
            . . . . . . e e 4 e . . . . . . 
            . . . . . . e 2 4 e . . . . . . 
            . . . . . c c c e e e . . . . . 
            . . . . e e 2 2 2 4 e e . . . . 
            . . c f f f c c e e f f e e . . 
            . c c c c e e 2 2 2 2 4 2 e e . 
            c c c c c c e e 2 2 2 4 2 2 e e 
            c c c c c c e e 2 2 2 2 4 2 e e
    """),
    SpriteKind.player)
mySprite.set_position(80, 100)
controller.move_sprite(mySprite, 100, 0)
mySprite.set_stay_in_screen(True)
info.set_score(0)
info.set_life(3)

def on_update_interval():
    global projectile2
    projectile2 = sprites.create_projectile_from_side(img("""
            . . . . . . . . . c c 8 . . . . 
                    . . . . . . 8 c c c f 8 c c . . 
                    . . . c c 8 8 f c a f f f c c . 
                    . . c c c f f f c a a f f c c c 
                    8 c c c f f f f c c a a c 8 c c 
                    c c c b f f f 8 a c c a a a c c 
                    c a a b b 8 a b c c c c c c c c 
                    a f c a a b b a c c c c c f f c 
                    a 8 f c a a c c a c a c f f f c 
                    c a 8 a a c c c c a a f f f 8 a 
                    . a c a a c f f a a b 8 f f c a 
                    . . c c b a f f f a b b c c 6 c 
                    . . . c b b a f f 6 6 a b 6 c . 
                    . . . c c b b b 6 6 a c c c c . 
                    . . . . c c a b b c c c . . . . 
                    . . . . . c c c c c c . . . . .
        """),
        0,
        randint(30, 100))
    projectile2.set_position(randint(0, 160), 0)
    animation.run_image_animation(projectile2,
        [img("""
                . . . . . . . . . c c 8 . . . . 
                        . . . . . . 8 c c c f 8 c c . . 
                        . . . c c 8 8 f c a f f f c c . 
                        . . c c c f f f c a a f f c c c 
                        8 c c c f f f f c c a a c 8 c c 
                        c c c b f f f 8 a c c a a a c c 
                        c a a b b 8 a b c c c c c c c c 
                        a f c a a b b a c c c c c f f c 
                        a 8 f c a a c c a c a c f f f c 
                        c a 8 a a c c c c a a f f f 8 a 
                        . a c a a c f f a a b 8 f f c a 
                        . . c c b a f f f a b b c c 6 c 
                        . . . c b b a f f 6 6 a b 6 c . 
                        . . . c c b b b 6 6 a c c c c . 
                        . . . . c c a b b c c c . . . . 
                        . . . . . c c c c c c . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . c c c c . . 
                        . c c c c c . c c c c c f c c . 
                        c c a c c c c c 8 f f c f f c c 
                        c a f a a c c a f f c a a f f c 
                        c a 8 f a a c a c c c a a a a c 
                        c b c f a a a a a c c c c c c c 
                        c b b a a c f 8 a c c c 8 c c c 
                        . c b b a b c f a a a 8 8 c c . 
                        . . . . a a b b b a a 8 a c . . 
                        . . . . c b c a a c c b . . . . 
                        . . . . b b c c a b b a . . . . 
                        . . . . b b a b a 6 a . . . . . 
                        . . . . c b b b 6 6 c . . . . . 
                        . . . . . c a 6 6 b c . . . . . 
                        . . . . . . . c c c . . . . . .
            """),
            img("""
                . . . . . . . . c c c c . . . . 
                        . . . . c c c c c c c c c . . . 
                        . . . c f c c a a a a c a c . . 
                        . . c c f f f f a a a c a a c . 
                        . . c c a f f c a a f f f a a c 
                        . . c c a a a a b c f f f a a c 
                        . c c c c a c c b a f c a a c c 
                        c a f f c c c a b b 6 b b b c c 
                        c a f f f f c c c 6 b b b a a c 
                        c a a c f f c a 6 6 b b b a a c 
                        c c b a a a a b 6 b b a b b a . 
                        . c c b b b b b b b a c c b a . 
                        . . c c c b c c c b a a b c . . 
                        . . . . c b a c c b b b c . . . 
                        . . . . c b b a a 6 b c . . . . 
                        . . . . . . b 6 6 c c . . . . .
            """),
            img("""
                . . . . . . . c c c a c . . . . 
                        . . c c b b b a c a a a c . . . 
                        . c c a b a c b a a a b c c . . 
                        . c a b c f f f b a b b b a . . 
                        . c a c f f f 8 a b b b b b a . 
                        . c a 8 f f 8 c a b b b b b a . 
                        c c c a c c c c a b c f a b c c 
                        c c a a a c c c a c f f c b b a 
                        c c a b 6 a c c a f f c c b b a 
                        c a b c 8 6 c c a a a b b c b c 
                        c a c f f a c c a f a c c c b . 
                        c a 8 f c c b a f f c b c c c . 
                        . c b c c c c b f c a b b a c . 
                        . . a b b b b b b b b b b b c . 
                        . . . c c c c b b b b b c c . . 
                        . . . . . . . . c b b c . . . .
            """),
            img("""
                . . . . . . c c c . . . . . . . 
                        . . . . . a a a c c c . . . . . 
                        . . . c a c f a a a a c . . . . 
                        . . c a c f f f a f f a c . . . 
                        . c c a c c f a a c f f a c . . 
                        . a b a a c 6 a a c c f a c c c 
                        . a b b b 6 a b b a a c a f f c 
                        . . a b b a f f b b a a c f f c 
                        c . a a a c c f c b a a c f a c 
                        c c a a a c c a a a b b a c a c 
                        a c a b b a a 6 a b b 6 b b c . 
                        b a c b b b 6 b c . c c a c . . 
                        b a c c a b b a c . . . . . . . 
                        b b a c a b a a . . . . . . . . 
                        a b 6 b b a c . . . . . . . . . 
                        . a a b c . . . . . . . . . . .
            """)],
        100,
        True)
    projectile2.set_kind(SpriteKind.enemy)
game.on_update_interval(500, on_update_interval)
