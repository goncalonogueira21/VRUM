var User = require('../models/user')

// Devolve a lista de Users
module.exports.listar = () => {
    return User
        .find()
        .exec()
}

module.exports.findByUserName = u => {
    return User
        .findOne({username: u})
        .exec()
}

module.exports.findByUserEmail = e => {
    return User
        .findOne({email: e})
        .exec()
}

module.exports.consultar = id => {
    return User
        .findOne({ _id: id })
        .exec()
}

module.exports.inserir = a => {
    var User1 = new User(a)
    return User1.save()
}

module.exports.eliminar = id => {
    return User.deleteOne({ _id: id })
}

module.exports.atualizar = (num, User) => {
    return User.updateOne({ _id: num }, User)
}