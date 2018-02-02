#include <boost/python.hpp>
#include "telegram/Client.h"

namespace bp=boost::python;

BOOST_PYTHON_MODULE (tdlib) {
    bp::class_<td::Client>("Client")
            .def("execute", &td::Client::execute)
            .def("receive", &td::Client::receive)
            .def("send", &td::Client::send);
    bp::scope in_client = bp::class_<td::Client>("Client");
    bp::class_<td::Client::Response>("Response")
            .add_property("id", &td::Client::Response::id)
            .add_property("object", &td::Client::Response::object);
    bp::class_<td::Client::Request>("Request")
            .add_property("id", &td::Client::Request::id)
            .add_property("function", &td::Client::Request::function);
}