type t = {
  description : string;
  mutable items : Item.t list;
  mutable exits : (string * t) list;
}

let create description items = { description; items; exits = [] }

let add_exit room direction room' =
  room.exits <- (direction, room') :: room.exits
