#include <boost/python.hpp>
#include "telegram/ClientActor.h"
#include "telegram/TdCallback.h"

namespace bp=boost::python;

BOOST_PYTHON_MODULE (tdlib) {
    bp::class_<td::ClientActor, bp::bases<td::Actor>>("ClientActor", bp::init<td::unique_ptr<td::TdCallback>>())
            .def("execute", &td::ClientActor::execute)
            .def("request", &td::ClientActor::request);
    bp::def("dump_pending_network_queries", td::dump_pending_network_queries);
}