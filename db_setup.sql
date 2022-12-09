create database if not exists PlaylistSong;
use PlaylistSong;

drop table if exists PlaylistSong.songs;

create table PlaylistSong.songs (
    song_id varchar(36) primary key,
    song_name varchar(30),
    artist_id varchar(30),
    artist_name varchar(30),
    album_id varchar(30),
    album_album varchar(30)
);