def player_scores(db, player_name):
    return db.search(f"""
    SELECT game_id, score 
        FROM Scores scr
            INNER JOIN Players plyr
                ON plyr.player_id=scr.player_id 
                AND plyr.player_name='{player_name}'
        """)

def shot_percent(db, player_name, ring='>0', face='>0', stack='>0'):
    return db.search_one(f"""
    SELECT
    (SELECT COUNT(*) FROM Throws thrw 
        INNER JOIN Players plyr 
                ON plyr.player_id=thrw.player_id
                AND thrw.ring_id{ring}
                AND thrw.face_id{face}
                AND thrw.stack_id{stack}
                AND plyr.player_name='{player_name}')
    /
    ((SELECT COUNT(*) FROM Throws thrw 
        INNER JOIN Players plyr 
            ON plyr.player_id=thrw.player_id 
            AND plyr.player_name='{player_name}')*.01)
    """)

def cumulative_score(db, player_name):
    return db.search(f"""
    SELECT game_id, SUM(score) OVER (ROWS UNBOUNDED PRECEDING)
        FROM Scores scr
            INNER JOIN Players plyr
                ON plyr.player_id=scr.player_id 
                AND plyr.player_name='{player_name}'
        """)

def cumulative_average(db, player_name):
    return db.search(f"""
    SELECT game_id, AVG(score) OVER (ROWS UNBOUNDED PRECEDING)
        FROM Scores scr
            INNER JOIN Players plyr
                ON plyr.player_id=scr.player_id 
                AND plyr.player_name='{player_name}'
        """)

def rolling_average(db, player_name, n):
    return db.search(f"""
    SELECT game_id, AVG(score) OVER (ROWS BETWEEN {n} PRECEDING AND CURRENT ROW)
        FROM Scores scr
            INNER JOIN Players plyr
                ON plyr.player_id=scr.player_id 
                AND plyr.player_name='{player_name}'
        """)

def cumulative_hits(db, player_name):
    return db.search(f"""
    SELECT (COUNT(*) OVER (ROWS UNBOUNDED PRECEDING)), (COUNT(NULLIF(points,0)) OVER (ROWS UNBOUNDED PRECEDING))*100.0/(COUNT(*) OVER (ROWS UNBOUNDED PRECEDING))
        FROM Throws thrw
            INNER JOIN Players plyr
                ON plyr.player_id=thrw.player_id 
                AND plyr.player_name='{player_name}'
        ORDER BY
            game_id ASC,
            toss_id ASC;
        """)
        
def game_shot_percent(db, player_name):
    hits = db.search(f"""
    SELECT game_id , points
        FROM Throws thrw
            INNER JOIN Players plyr
                ON plyr.player_id=thrw.player_id 
                AND plyr.player_name='{player_name}'
        ORDER BY
            game_id ASC,
            toss_id ASC;
        """)
    games = [[0, 0]] # (game_id, points)
    for h in hits:
        if games[-1][0] == h[0]:
            games[-1][1] += int(bool(h[1]))
        else:
            games[-1][1] = games[-1][1]/.09
            games.append([h[0], int(bool(h[1]))])
    games.pop(0)
    games.pop(-1)
    return games