type t = {
  mutable current_room : Room.t;
  mutable inventory : Item.t list;
}

let create current_room = { current_room; inventory = [] }

let move player direction =
  match List.assoc_opt direction player.current_room.Room.exits with
  | Some room -> player.current_room <- room
  | None -> print_endline "You can't go that way."

let pick_up player item =
  if List.mem item player.current_room.Room.items then begin
    player.current_room.Room.items <- List.filter ((<>) item) player.current_room.Room.items;
    player.inventory <- item :: player.inventory;
    print_endline ("You picked up the " ^ item.Item.name ^ ".")
  end else
    print_endline "That item is not here."
