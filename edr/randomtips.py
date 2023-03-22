#!/usr/bin/env python
# coding=utf-8

import os
import json
import random

import edri18n
import utils2to3

def _(message): return message

DEFAULT_TIPS = {
    "edr": [
        _(u"Situation reports (SITREPs) provide a summary of recent activity at a location."),
        _(u"Send !sitreps in chat to get a list of systems with recent activity."),
        _(u"Send !sitrep <system> in chat to get a SITREP for <system>, e.g. !sitrep Lave."),
        _(u"A Notice to Airmen (NOTAM) warns pilots about potential hazards at a location."),
        _(u"Send '!notams' in chat to get a list of systems with Notice to Airmen, i.e. NOTAM."),
        _(u"Send '!notam <system>' in chat to see the NOTAMs associated with a given system, e.g. !notam Lave."),
        _(u"EDR does NOT report crimes committed in Anarchy or Lawless systems."),
        _(u"Scans of SRV are not reported by Elite Dangerous. So, direct message an o7 to run a profile lookup on SRV contacts."),
        _(u"EDR disables itself in Solo, Private Groups and Beta."),
        _(u"Send '!crimes off' in chat to disable EDR's crime reporting, e.g. arranged duel."),
        _(u"Send '!crimes on' in chat to re-enable EDR's crime reporting."),
        _(u"Send '!audiocue soft' in chat if the audio cues are too loud."),
        _(u"Send '!audiocue loud' in chat if the audio cues are too soft."),
        _(u"Send '!audiocue off' in chat to disable the audio cues."),
        _(u"Send '!audiocue on' in chat to enable the audio cues."),
        _(u"Report suspicious contacts by sending them a direct message."),
        _(u"Send an 'o7' to a contact to learn more about them (i.e. inara profile, EDR insights)."),
        _(u"EDR will automatically report interdictions and deaths to help bounty hunters and law enforcers."),
        _(u"Send '!who <cmdrname> in chat to learn more about <cmdrname>, e.g. !who lekeno"),
        _(u"Send '!overlay off' in chat to disable the in-game overlay."),
        _(u"Send '!overlay on' in chat to enable the in-game overlay."),
        _(u"Send '!overlay' in chat to check the status of the in-game overlay."),
        _(u"Follow the instructions in igm_config.ini to customize EDR's layout."),
        _(u"EDR will automatically report other commanders if they say something on local chat."),
        _(u"EDR will automatically report other commanders if they direct message you (unless they are on your friends list)."),
        _(u"EDR will warn you about outlaws if they reveal themselves or if you report them"),
        _(u"Your EDR account is tied to your cmdr name, do NOT share your credentials with someone else or a different cmdr account."),
        _(u"Sending '-#' to a contact will remove them from your commanders index."),
        _(u"Send '-# <cmdrname>' to remove <cmdrname> from your commanders index."),
        _(u"Sending '#!' or '#outlaw' to a contact will tag them as an outlaw in your commanders index."),
        _(u"Send '#! <cmdrname>' or '#outlaw <cmdrname>' to tag <cmdrname> as an outlaw in your commanders index."),
        _(u"Sending '#?' or '#neutral' to a contact will tag them as neutral in your commanders index."),
        _(u"Send '#? <cmdrname>' or '#neutral <cmdrname>' to tag <cmdrname> as neutral in your commanders index."),
        _(u"Sending '#+' or '#enforcer' to a contact will tag them as an enforcer in your commanders index."),
        _(u"Send '#+ <cmdrname>' or '#enforcer <cmdrname>' to tag <cmdrname> as an enforcer in your commanders index."),
        _(u"Sending '#=' or '#friend' to a contact will tag them as a friend in your commanders index."),
        _(u"Send '#= <cmdrname>' or '#friend <cmdrname>' to tag <cmdrname> as a friend in your commanders index."),
        _(u"Sending '#<tag>' to a contact will tag them as <tag> in your commanders index."),
        _(u"Send '#<tag> <cmdrname>' to tag <cmdrname> as <tag> in your commanders index."),
        _(u"Sending '#s!' or '#enemy' to a contact will tag them as an enemy for your Inara squadron."),
        _(u"Send '#s! <cmdrname>' or '#enemy <cmdrname>' to tag <cmdrname> as an enemy for your Inara squadron."),
        _(u"Sending '#s+' or '#ally' to a contact will tag them as an ally for your Inara squadron."),
        _(u"Send '#s+ <cmdrname>' or '#ally <cmdrname>' to tag <cmdrname> as an ally for your Inara squadron."),
        _(u"EDR will use the friend tag to infer a social graph for upcoming features."),
        _(u"Your commanders index is personal. EDR will only show aggregate stats to other EDR users."),
        _(u"Tag a commander with an outlaw tag if you witness them going after a clean and non-enemy power commander."),
        _(u"Tag a pirate with an outlaw tag if you witness them destroying a co-operating ship."),
        _(u"Tag a commander with an enforcer tag if you have seen them going after an outlaw."),
        _(u"Tag a commander with a neutral tag if you disagree with EDR's classification."),
        _(u"Tag a commander with a friend tag if you are like-minded and/or fly often together."),
        _(u"Tag a commander with a custom tag for your own needs, e.g. #pirate."),
        _(u"Sending '@# <memo>' to a contact will attach a custom note with <memo> in your commanders index."),
        _(u"Sending '@# <cmdrname> memo=<memo>' will attach a custom note with <memo> on <cmdrname> in your commanders index."),
        _(u"Send '-@' to a contact to remove any attached note in your commanders index."),
        _(u"Send '-@ <cmdrname>' to remove the note attached to <cmdrname> in your commanders index."),
        _(u"In an Intel response, [!70% ?20% +10%] shows the percentage of outlaw (!), neutral (?) and enforcer (+) tags set by other EDR users."),
        _(u"In an Intel response, [!3 ?0 +0] shows the number of outlaw (!), neutral (?) and enforcer (+) tags set by other EDR users."),
        _(u"Have a suggestion for a tip? File an issue at https://github.com/lekeno/edr/issues"),
        _(u"Found a bug? File an issue at https://github.com/lekeno/edr/issues"),
        _(u"Have a feature request? File an issue at https://github.com/lekeno/edr/issues"),
        _(u"Do you like EDR? Consider supporting its development and hosting costs at https://patreon.com/lekeno"),
        _(u"Send '!where <cmdrname>' to find out where an outlaw/enemy was last sighted"),
        _(u"Send '!outlaws' to find out where outlaws were last sighted"),
        _(u"Send '?outlaws on': to enable realtime alerts for sighted outlaws."),
        _(u"Send '?outlaws off': to disable realtime alerts for sighted outlaws."),
        _(u"Send '?outlaws': to check the state and configuration of the realtime alerts for sighted outlaws."),
        _(u"Send '?outlaws ly 150': to configure a maximal distance of 150 ly for the outlaws realtime alerts."),
        _(u"Send '?outlaws cr 10000': to configure a minimal bounty of 10k cr for the outlaws realtime alerts."),
        _(u"Send '?outlaws cr -': to remove the minimal bounty for the realtime alerts."),
        _(u"Send '?outlaws ly -': to remove the maximal distance for the realtime alerts."),
        _(u"Send '!clear' to clear everything on EDR's overlay"),
        _(u"Send '!enemies' to find out where enemies were last sighted"),
        _(u"Send '?enemies on': to enable realtime alerts for sighted enemies."),
        _(u"Send '?enemies off': to disable realtime alerts for sighted enemies."),
        _(u"Send '?enemies': to check the state and configuration of the realtime alerts for sighted enemies."),
        _(u"Send '?enemies ly 150': to configure a maximal distance of 150 ly for the enemies realtime alerts."),
        _(u"Send '?enemies cr 10000': to configure a minimal bounty of 10k cr for the enemies realtime alerts."),
        _(u"Send '?enemies cr -': to remove the minimal bounty for the realtime alerts."),
        _(u"Send '?enemies ly -': to remove the maximal distance for the realtime alerts."),
        _(u"Send '!distance <system>' or '!d <system>': shows the distance to <system>."),
        _(u"Send '!distance Lave > Eravate' or '!d Lave > Eravate': shows the distance from Lave to Eravate."),
        _(u"Send '!search resource name', e.g. '!search cadmium', to find the closest hotspot for rare resources."),
        _(u"Send '!if' or '!if Lave' to find an Interstellar Factors near your position or a specific system."),
        _(u"Send '!raw' or '!raw Lave' to find a Raw Material Trader near your position or a specific system."),
        _(u"Send '!encoded', !enc' or '!enc Lave' to find an Encoded Data Trader near your position or a specific system."),
        _(u"Send '!manufactured', '!man' or '!man Lave' to find a Manufactured Material Trader near your position or a specific system."),
        _(u"Send '!staging' or '!staging Lave' to find a good staging station near your position or a specific system, i.e. large pads, shipyard, outfitting, repair/rearm/refuel."),
        _(u"Send '!htb', '!humantechbroker' or '!htb Lave' to find a Human Tech Broker near your position or a specific system"),
        _(u"Send '!gtb', '!guardiantechbroker' or '!gtb Lave' to find a Guardian Tech Broker near your position or a specific system"),
        _(u"Send '!edr optional message' to dispatch a generic message to EDR Central's discord server (be mindful)."),
        _(u"Send '!911 optional message' to dispatch a law enforcer request to EDR Central's discord server (be mindful)."),
        _(u"Send '!fuel optional message' to dispatch a fuel request to EDR Central's discord server (be mindful). Also, check the UI in EDMC for Fuel Rats/Corgis instructions."),
        _(u"Send '!repair optional message' to dispatch a repair request to EDR Central's discord server (be mindful). Also, check the UI in EDMC for Repair Corgis instructions."),
        _(u"Send '!nav 45.3 -3.5' for getting planetary guidance to a specific location, e.g. 45.3 longitude, -3.5 latitude."),
        _(u"Send '!nav off' to clear the navigation data."),
        _(u"Send '!nav set' to mark your current location as your navigation target."),
        _(u"Send '!ship fdl' to find out where you've parked your Fer-de-Lance."),
        _(u"Send '!ship In Front Of Things' to find out where you've parked your ship named 'In Front of Things'."),
        _(u"Send '!eval power' to get an assessment of your power priorities."),
        _(u"[Odyssey] Send '!eval backpack' to get an assessment of items in your backpack."),
        _(u"[Odyssey] Send '!eval locker' to get an assessment of items in your ship locker."),
        _(u"[Odyssey] Send '!eval bar' to get an assessment of items on sale from the last visited bar on a fleet carrier."),
        _(u"[Odyssey] Send '!eval bar demand' to get an assessment of items in demand at the last visited bar on a fleet carrier."),
        _(u"Send '!offbeat' to get a station whose info hasn't been updated recently and has a higher chance of carrying premium weapons/suits."),
        _(u"Send '!materials' to get a list of material profiles supported by EDR (e.g. synthesis for FSD, etc.)"),
        _(u"Send '!rrrfc' to get a fleet carrier with repair, rearm, refuel in the current system. Double check docking access before proceeding."),
        _(u"Send '!rrrfc < 15' to get a fleet carrier with repair, rearm, refuel within 15 LY of the current system. Double check docking access before proceeding."),
        _(u"Send '!rrrfc deciat' to get a fleet carrier with repair, rearm, refuel within the specified system (e.g. Deciat). Double check docking access before proceeding."),
        _(u"Send '!rrr' to get a station with repair, rearm, refuel in the current system."),
        _(u"Send '!rrr < 15' to get a station with repair, rearm, refuel within 15 LY of the current system."),
        _(u"Send '!rrr deciat' to get a station with repair, rearm, refuel within the specified system (e.g. Deciat)."),
        _(u"Send 'When using EDR's search features, the system name will be placed in the clipboard. Hit Ctrl+V to paste the result."),
        _(u"Send '!parking' to check for fleet carrier parking slots in the current system."),
        _(u"Send '!parking #1' to check for fleet carrier parking slots in the first system near your location."),
        _(u"Send '!parking deciat' to check for fleet carrier parking slots in Deciat."),
        _(u"Send '!parking deciat #3' to check for fleet carrier parking slots in the third closest system to Deciat."),
        _(u"Send '!fc J6B' to display info for a local fleet carrier whose callsign or name contains J6B."),
        _(u"Send '!station Jameson' to display info for a local station/outpost/... whose name contains Jameson."),
        _(u"Point at materials with the emote gesture to identify them and have EDR share some info about how useful the material is."),
        _(u"Point at, or salute other players with the emote gestures to show their EDR and Inara profile."),
        _(u"When visiting a bar on a fleet carrier, EDR will list the most useful Odyssey items that are on sale if any."),
        _(u"When visiting a bar on a fleet carrier with no items on sale, EDR will list the least useful Odyssey items that can be sold if any."),
        _(u"Send !tip for a random advice; Send '!tip edr' for an EDR related advice, or '!tip open' for an advice about playing in Open"),
        _(u"Send '!nav next' or '!nav previous' when near/on a planet to select the next/previous custom Point of Interest."),
        _(u"Send '!nav clear' or the 'stop' gesture when near/on a planet to clear the current custom Point of Interest."),
        _(u"Send '!nav reset' when near/on a planet to clear all the custom Point of Interests."),
        _(u"When targeting or approaching a planet, EDR will provide exobiology insights if the planet is suitable."),
        _(u"EDR will automatically add a custom Point of Interest when scanning biological element with the composition scanner."),
        _(u"EDR will automatically add a custom Point of Interest when pointing at something while on foot (current location)."),
        _(u"After scanning a biological with the genetic sampler, EDR will show the value of the specimen, the minimum distance for gene diversity, the distance and heading for the previous samples."),
        _(u"If you stumble upon another species while doing Exobiology research, consider using the 'pointing' gesture to record your current position as a custom Point of Interest so that you can find it back later."),
        _(u"Custom Point of Interests on planets are not persistent (i.e. will disappear if you close EDMC)."),
        _(u"Send '!search bio' to find a nearby planet with the right conditions for exobiology."),
        _(u"Send '!search water' to find a nearby planet with a water atmosphere (rich in exobiology)."),
        _(u"Send '!search ammonia' to find a nearby planet with an ammonia atmospehere."),
        _(u"You can use the !search command to find a nearby planet with the right conditions for a given genus, e.g. '!search stratum'"),
        _(u"You can use the !search command to find a nearby planet with the right conditions for a given species, e.g. '!search stratum tectonicas'")
    ],
    "open": [
        _(u"Never fly what you can't afford to lose. Check your rebuy and credit balance on your right panel."),
        _(u"Never combat log in Open. If you aren't willing to accept the risk, don't bother with Open, Google 'Mobius PVE'."),
        _(u"Hit Ctrl+B to display a bandwidth meter. You are not alone if it goes over 1000 B/s."),
        _(u"Regularly check your contact history in the top panel for known threats."),
        _(u"[Planet] Dismiss your ship immediately after boarding your SRV. Outlaws will destroy it in seconds otherwise."),
        _(u"[Planet] Switch your SRV lights off if an outlaw shows up. Run far away before calling back your ship."),
        _(u"[Planet] For new discoveries, land a bit away from the area of interest and dismiss your ship asap."),
        _(u"[Explorers] Don't trust anyone, check a contact's loadout in your left panel before banding to take selfies."),
        _(u"[Explorers] On your trip back to the bubble, reach out to Iridium Wing for an escort."),
        _(u"[Explorers] Throttle down to 0% when your jump completes to avoid bad surprises (e.g. neutron star, 2 stars close to each other)"),
        _(u"[Traders] Don't be greedy, use your biggest slot for a shield not for cargo!"),
        _(u"[Traders] Pledge for 4 weeks to Aisling Duval in order to get the stronger 'prismatic shields'."),
        _(u"[Traders] Engineer regular shields with Thermal Resistance, shield boosters with Heavy Duty."),
        _(u"[Traders] Engineer prismatic shields with Reinforced, even resistance % with Augmented Resistance on your shield boosters."),
        _(u"[Traders] Rares are special goods (e.g. Hutton Mug, Sothis Gold). The further you take them from where you buy them (up to 200ly) the more you get for them."),
        _(u"[Suicide trap] At busy stations, stay below 100 m/s or you will get killed by the station for colliding into a 'suicide eagle'."),
        _(u"[Suicide trap] Advanced trap: force shells may push you over the 100m/s safe speed limit. Watch out for wings/duo and cannons loadouts."),
        _(u"[Anti-suicide trap] Buy an eagle, remove its shield, ram the suicide eagle before they destroy another ship."),
        _(u"[Anti-suicide trap] Stay under 100 m/s and ram the suicide eagle before they destroy another ship."),
        _(u"[Anti-suicide trap] Warn other commanders about the presence of a 'suicide eagle' as they approach or leave the station."),
        _(u"[Powerplay hunters] Watch out for powerplay hunters at stations in enemy territory: fighting back will get you wanted."),
        _(u"[Anarchy] Watch for suspicious pilots, they can safely hunt/ram you even if you are clean (station and security won't retaliate)."),
        _(u"[Station] The station fires back when hit. Use that to your advantage: stay close to the structure, chaff, etc."),
        _(u"[Station] The no-fire zone is a misnomer: players can and will fire at you at the cost of a small fine."),
        _(u"[Escape] Bind a key/button to 'select next route' to quickly target your escape route."),
        _(u"[Escape] It is safer and faster to jump to a different system than going back to supercruise (i.e. 'high waking' is not subject to mass lock)."),
        _(u"[Interdiction] Do NOT attempt to win a player interdiction, instead submit to get a faster FSD cooldown."),
        _(u"[Interdiction] Type-7's have a high yaw rate which comes handy when fighting interdictions."),
        _(u"[Community Goal] Consider setting camp at a nearby system with a decent station instead of going straight for the CG system/station"),
        _(u"[Community Goal] Drop just before being interdicted, throttle to zero, charge your FSD, boost when the player shows up. Repeat."),
        _(u"[Supercruise] Don't supercruise straight to the station, take a curve above the plane: faster and safer."),
        _(u"[Supercruise] Go around planets and other stellar objects as they will slow you down."),
        _(u"[Supercruise] 'Ride the 6': keep max speed until the countdown reaches 6 seconds, then middle of the blue zone."),
        _(u"[Supercruise] If your destination is near a planet, have the planet behind you and use its gravity well to slow you down."),
        _(u"[Combat] Put all 4 pips to SYS when being fired upon; move them where needed when not fired upon."),
        _(u"[Combat] Don't fly in a straight line, you'll die if you do. Be evasive: combine rolls, turns, thrusters, boost and Fligh Assist Off."),
        _(u"[Combat] When shields drop, target specific modules. In particular: power plant, drives, biweave shields, weapons."),
        _(u"[Combat] Double shield cell banking: fire first cell, wait for 90 percents heat, fire heat sink, when heat drops rapidly fire the second cell."),
        _(u"[Combat] Railgun with feedback cascade can counter shield cell banking."),
        _(u"[Combat] Best time to fire your shield cell is when you are at 1 / 1.5 ring and right in front of your opponent just as you are about to fly past them."),
        _(u"[Interdicted] Put 4 pips to SYS, 2 to ENG and fly evasive. Hit next route and high wake asap, do not fly in a straight line."),
        _(u"[Pirates] Follow their instructions and you will avoid a certain death."),
        _(u"[Fuel] Mnemonics for fuel scoopable stars: KGB FOAM or 'Oh Be A Fine Girl Kiss Me'."),
        _(u"[Fuel] Out of fuel? Call the fuel rats (https://fuelrats.com/)."),
        _(u"[Bounty hunting] Don't steal kills. Instead, ask to join a wing: everyone will get the same bounty and way faster."),
        _(u"[Community] Most players are just nice folks. Chat with people, make friends. It might come handy."),
        _(u"[Defense] Fit Point Defenses to your ship to destroy missiles and mines"),
        _(u"[Defense] Like the song says you've got to know when to walk away and know when to run."),
        _(u"[Mining] Limit your cargo (e.g. LTD) to be within 10 percents of the demand of a market in order to get the highest price.")
    ]
}

del _

class RandomTips(object):

    def __init__(self, tips_file=None):
        global DEFAULT_TIPS
        if tips_file:
            self.tips = json.loads(open(utils2to3.abspathmaker(__file__, tips_file)).read())
        else:
            self.tips = DEFAULT_TIPS

    def tip(self, category=None):
        random.seed()
        if category not in self.tips:
            category = random.choice(list(self.tips))
        else:
            category = category.lower()
        return edri18n._(random.choice(self.tips[category]))