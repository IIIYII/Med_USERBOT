# Med - UserBot
# Copyright (c) 2022 Med_USERBOT
# Credits: @MedThon || https://github.com/MedThon
#
# This file is a part of < https://github.com/IIIYII/Med_USERBOT >
# t.me/MedThon & t.me/L_U_2

QUEUE = {}


def add_to_queue(chat_id, songname, link, ref, type, quality):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([songname, link, ref, type, quality])
        return int(len(chat_queue) - 1)
    QUEUE[chat_id] = [[songname, link, ref, type, quality]]


def get_queue(chat_id):
    if chat_id in QUEUE:
        return QUEUE[chat_id]
    return 0


def pop_an_item(chat_id):
    if chat_id not in QUEUE:
        return 0

    chat_queue = QUEUE[chat_id]
    chat_queue.pop(0)
    return 1


def clear_queue(chat_id: int):
    if chat_id not in QUEUE:
        return 0

    QUEUE.pop(chat_id)
    return 1
