let rec game_loop player =
  print_endline player.Player.current_room.Room.description;
  print_string "> ";
  match read_line () with
  | "quit" -> ()
  | command -> handle_command player command; game_loop player

and handle_command player command =
  match String.split_on_char ' ' command with
  | "go" :: direction :: _ -> Player.move player direction
  | "get" :: item_name :: _ ->
    let item = List.find_opt (fun item -> item.Item.name = item_name) player.Player.current_room.Room.items in
    (match item with
     | Some item -> Player.pick_up player item
     | None -> print_endline "That item is not here.")
  | _ -> print_endline "I don't understand that command."
