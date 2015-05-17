# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint
from frappe.model.document import Document

class Project(Document):
	def validate(self):
		self.calculate_totals()
		self.set_zone()
		
	def calculate_totals(self):
		self.total = cint(self.home_club) + cint(self.other_club) + cint(self.dcm) \
			+ cint(self.alumini) + cint(self.rotarians) + cint(self.pis) + cint(self.guest)

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")