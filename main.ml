open Room
open Player

let main () =
  let room1 = Room.create "You are in a small room. There is a door to the north." [] in
  let room2 = Room.create "You are in a large room. There is a door to the south." [] in
  Room.add_exit room1 "north" room2;
  Room.add_exit room2 "south" room1;
  let player = Player.create room1 in
  game_loop player

let () = main ()
